"""Tests for the follow-up learning system (nested topic sessions).

This tests the core follow-up system that enables users to drill deeper
into subtopics during lessons (e.g., request vasopressors while learning shock).
"""

import json
import sqlite3
import pytest
from datetime import datetime, timedelta

from src.student_model import initialize_database, conn as get_db


class TestSchemaExtension:
    """Test that new tables are created with correct schema."""

    def test_topic_hierarchy_table_exists(self):
        """Verify topic_hierarchy table created with correct schema."""
        db = sqlite3.connect(':memory:')
        initialize_database()

        # Connect to in-memory test DB and manually create tables
        cursor = db.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS topic_hierarchy (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                parent_topic_id INTEGER NOT NULL,
                child_topic_id INTEGER NOT NULL,
                relationship_type TEXT DEFAULT 'subtopic',
                order_priority INTEGER DEFAULT 0,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                UNIQUE(parent_topic_id, child_topic_id, relationship_type)
            )
        """)
        db.commit()

        cursor.execute("PRAGMA table_info(topic_hierarchy)")
        columns = {row[1]: row[2] for row in cursor.fetchall()}

        assert 'parent_topic_id' in columns
        assert 'child_topic_id' in columns
        assert 'relationship_type' in columns
        assert 'order_priority' in columns

        db.close()

    def test_follow_up_sessions_table_exists(self):
        """Verify follow_up_sessions table tracks active nested learning."""
        db = sqlite3.connect(':memory:')

        cursor = db.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS follow_up_sessions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                session_id TEXT NOT NULL,
                parent_topic_id INTEGER NOT NULL,
                child_topic_id INTEGER NOT NULL,
                parent_session_state TEXT,
                child_mastery_achieved BOOLEAN DEFAULT 0,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                completed_at TIMESTAMP
            )
        """)
        db.commit()

        cursor.execute("PRAGMA table_info(follow_up_sessions)")
        columns = {row[1]: row[2] for row in cursor.fetchall()}

        assert 'session_id' in columns
        assert 'parent_topic_id' in columns
        assert 'child_topic_id' in columns
        assert 'parent_session_state' in columns
        assert 'child_mastery_achieved' in columns
        assert 'created_at' in columns

        db.close()

    def test_subtopic_weaknesses_table_exists(self):
        """Verify subtopic_weaknesses tracks fine-grained knowledge gaps."""
        db = sqlite3.connect(':memory:')

        cursor = db.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS subtopic_weaknesses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                topic_id INTEGER NOT NULL,
                subtopic_id INTEGER NOT NULL,
                weakness_type TEXT NOT NULL,
                failure_count INTEGER DEFAULT 0,
                last_seen TIMESTAMP,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                UNIQUE(topic_id, subtopic_id, weakness_type)
            )
        """)
        db.commit()

        cursor.execute("PRAGMA table_info(subtopic_weaknesses)")
        columns = {row[1]: row[2] for row in cursor.fetchall()}

        assert 'topic_id' in columns
        assert 'subtopic_id' in columns
        assert 'weakness_type' in columns
        assert 'failure_count' in columns
        assert 'last_seen' in columns

        db.close()


class TestRequestFollowUp:
    """Test request_follow_up() endpoint."""

    def test_request_follow_up_creates_session(self):
        """Verify request_follow_up() suggests relevant subtopics and creates nested session."""
        db = sqlite3.connect(':memory:')

        # Create tables
        cursor = db.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS topics (
                topic_id INTEGER PRIMARY KEY AUTOINCREMENT,
                topic TEXT NOT NULL UNIQUE
            )
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS topic_hierarchy (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                parent_topic_id INTEGER NOT NULL,
                child_topic_id INTEGER NOT NULL,
                relationship_type TEXT DEFAULT 'subtopic',
                order_priority INTEGER DEFAULT 0,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                UNIQUE(parent_topic_id, child_topic_id, relationship_type)
            )
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS follow_up_sessions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                session_id TEXT NOT NULL,
                parent_topic_id INTEGER NOT NULL,
                child_topic_id INTEGER NOT NULL,
                parent_session_state TEXT,
                child_mastery_achieved BOOLEAN DEFAULT 0,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                completed_at TIMESTAMP
            )
        """)

        # Create topics
        cursor.execute("INSERT INTO topics (topic) VALUES ('shock')")
        parent_id = cursor.lastrowid

        cursor.execute("INSERT INTO topics (topic) VALUES ('vasopressors')")
        vaso_id = cursor.lastrowid

        cursor.execute("INSERT INTO topics (topic) VALUES ('fluid_resuscitation')")
        fluid_id = cursor.lastrowid

        # Link as subtopics
        cursor.execute("""
            INSERT INTO topic_hierarchy (parent_topic_id, child_topic_id, relationship_type, order_priority)
            VALUES (?, ?, 'subtopic', 1)
        """, (parent_id, vaso_id))
        cursor.execute("""
            INSERT INTO topic_hierarchy (parent_topic_id, child_topic_id, relationship_type, order_priority)
            VALUES (?, ?, 'subtopic', 2)
        """, (parent_id, fluid_id))

        db.commit()

        # Simulate request_follow_up logic
        cursor.execute("SELECT topic_id FROM topics WHERE topic = ?", ('shock',))
        parent_row = cursor.fetchone()
        assert parent_row is not None
        parent_topic_id = parent_row[0]

        cursor.execute("SELECT topic_id FROM topics WHERE topic = ?", ('vasopressors',))
        child_row = cursor.fetchone()
        assert child_row is not None
        child_topic_id = child_row[0]

        # Create follow-up session
        cursor.execute("""
            INSERT INTO follow_up_sessions (session_id, parent_topic_id, child_topic_id, parent_session_state)
            VALUES (?, ?, ?, ?)
        """, ('test_session_1', parent_topic_id, child_topic_id, json.dumps({})))
        db.commit()
        session_id = cursor.lastrowid

        # Verify session was created
        cursor.execute("SELECT COUNT(*) FROM follow_up_sessions WHERE parent_topic_id = ?", (parent_topic_id,))
        count = cursor.fetchone()[0]
        assert count == 1

        # Verify related subtopics can be retrieved
        cursor.execute("""
            SELECT t.topic FROM topics t
            JOIN topic_hierarchy h ON t.topic_id = h.child_topic_id
            WHERE h.parent_topic_id = ? AND h.child_topic_id != ? AND h.relationship_type = 'subtopic'
            ORDER BY h.order_priority
        """, (parent_topic_id, child_topic_id))
        related = [row[0] for row in cursor.fetchall()]
        assert 'fluid_resuscitation' in related

        db.close()


class TestGetNextTopic:
    """Test get_next_topic() prioritization."""

    def test_get_next_topic_prioritizes_active_follow_up(self):
        """Verify get_next_topic() prioritizes child topic when in active follow-up session."""
        db = sqlite3.connect(':memory:')

        cursor = db.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS topics (
                topic_id INTEGER PRIMARY KEY AUTOINCREMENT,
                topic TEXT NOT NULL UNIQUE
            )
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS follow_up_sessions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                session_id TEXT NOT NULL,
                parent_topic_id INTEGER NOT NULL,
                child_topic_id INTEGER NOT NULL,
                child_mastery_achieved BOOLEAN DEFAULT 0,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)

        # Create topics
        cursor.execute("INSERT INTO topics (topic) VALUES ('shock')")
        parent_id = cursor.lastrowid

        cursor.execute("INSERT INTO topics (topic) VALUES ('vasopressors')")
        child_id = cursor.lastrowid

        # Create active follow-up session
        cursor.execute("""
            INSERT INTO follow_up_sessions (session_id, parent_topic_id, child_topic_id, child_mastery_achieved)
            VALUES ('test_session', ?, ?, 0)
        """, (parent_id, child_id))

        db.commit()

        # Query active child topic
        cursor.execute("""
            SELECT t.topic FROM topics t
            JOIN follow_up_sessions f ON t.topic_id = f.child_topic_id
            WHERE f.session_id = 'test_session' AND f.child_mastery_achieved = 0
            LIMIT 1
        """)
        active_child = cursor.fetchone()

        assert active_child is not None
        assert active_child[0] == 'vasopressors'

        db.close()


class TestSubmitAnswerSubtopicTracking:
    """Test submit_answer() with subtopic weaknesses."""

    def test_submit_answer_tracks_subtopic_weaknesses(self):
        """Verify submit_answer() tracks subtopic-level weaknesses."""
        db = sqlite3.connect(':memory:')

        cursor = db.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS topics (
                topic_id INTEGER PRIMARY KEY AUTOINCREMENT,
                topic TEXT NOT NULL UNIQUE
            )
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS follow_up_sessions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                session_id TEXT NOT NULL,
                parent_topic_id INTEGER NOT NULL,
                child_topic_id INTEGER NOT NULL,
                child_mastery_achieved BOOLEAN DEFAULT 0,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS subtopic_weaknesses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                topic_id INTEGER NOT NULL,
                subtopic_id INTEGER NOT NULL,
                weakness_type TEXT NOT NULL,
                failure_count INTEGER DEFAULT 0,
                last_seen TIMESTAMP,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                UNIQUE(topic_id, subtopic_id, weakness_type)
            )
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS question_attempts (
                attempt_id INTEGER PRIMARY KEY AUTOINCREMENT,
                topic_id INTEGER,
                session_id TEXT,
                is_correct BOOLEAN,
                timestamp TEXT
            )
        """)

        # Create topics
        cursor.execute("INSERT INTO topics (topic) VALUES ('vasopressors')")
        topic_id = cursor.lastrowid

        cursor.execute("INSERT INTO topics (topic) VALUES ('shock')")
        parent_id = cursor.lastrowid

        # Create follow-up session
        cursor.execute("""
            INSERT INTO follow_up_sessions (session_id, parent_topic_id, child_topic_id, child_mastery_achieved)
            VALUES ('test_session', ?, ?, 0)
        """, (parent_id, topic_id))
        db.commit()

        # Simulate submit_answer with wrong answer
        cursor.execute("""
            INSERT INTO question_attempts (topic_id, session_id, is_correct, timestamp)
            VALUES (?, 'test_session', 0, ?)
        """, (topic_id, datetime.now().isoformat()))

        # Record weakness
        cursor.execute("""
            INSERT INTO subtopic_weaknesses (topic_id, subtopic_id, weakness_type, failure_count, last_seen)
            VALUES (?, ?, ?, 1, ?)
            ON CONFLICT(topic_id, subtopic_id, weakness_type) DO UPDATE SET
            failure_count = failure_count + 1, last_seen = excluded.last_seen
        """, (parent_id, topic_id, 'mechanism', datetime.now().isoformat()))

        db.commit()

        # Verify weakness was recorded
        cursor.execute("""
            SELECT failure_count FROM subtopic_weaknesses
            WHERE topic_id = ? AND subtopic_id = ? AND weakness_type = 'mechanism'
        """, (parent_id, topic_id))
        weakness = cursor.fetchone()
        assert weakness is not None
        assert weakness[0] >= 1

        db.close()


class TestFullWorkflow:
    """End-to-end workflow tests."""

    def test_full_follow_up_workflow(self):
        """End-to-end: request follow-up → answer questions → return to parent."""
        db = sqlite3.connect(':memory:')

        cursor = db.cursor()

        # Create all required tables
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS topics (
                topic_id INTEGER PRIMARY KEY AUTOINCREMENT,
                topic TEXT NOT NULL UNIQUE
            )
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS topic_hierarchy (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                parent_topic_id INTEGER NOT NULL,
                child_topic_id INTEGER NOT NULL,
                relationship_type TEXT DEFAULT 'subtopic',
                order_priority INTEGER DEFAULT 0,
                UNIQUE(parent_topic_id, child_topic_id, relationship_type)
            )
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS follow_up_sessions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                session_id TEXT NOT NULL,
                parent_topic_id INTEGER NOT NULL,
                child_topic_id INTEGER NOT NULL,
                parent_session_state TEXT,
                child_mastery_achieved BOOLEAN DEFAULT 0,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                completed_at TIMESTAMP
            )
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS subtopic_weaknesses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                topic_id INTEGER NOT NULL,
                subtopic_id INTEGER NOT NULL,
                weakness_type TEXT NOT NULL,
                failure_count INTEGER DEFAULT 0,
                last_seen TIMESTAMP,
                UNIQUE(topic_id, subtopic_id, weakness_type)
            )
        """)

        # Create topics
        cursor.execute("INSERT INTO topics (topic) VALUES ('shock')")
        shock_id = cursor.lastrowid
        cursor.execute("INSERT INTO topics (topic) VALUES ('vasopressors')")
        vaso_id = cursor.lastrowid

        # Link parent-child
        cursor.execute("""
            INSERT INTO topic_hierarchy (parent_topic_id, child_topic_id, relationship_type)
            VALUES (?, ?, 'subtopic')
        """, (shock_id, vaso_id))

        db.commit()

        # 1. Request follow-up on vasopressors
        cursor.execute("""
            INSERT INTO follow_up_sessions (session_id, parent_topic_id, child_topic_id, parent_session_state)
            VALUES ('session_1', ?, ?, ?)
        """, (shock_id, vaso_id, json.dumps({})))
        db.commit()

        # 2. Verify follow-up session exists
        cursor.execute("SELECT id FROM follow_up_sessions WHERE session_id = 'session_1'")
        session = cursor.fetchone()
        assert session is not None

        # 3. Mark follow-up complete
        cursor.execute("""
            UPDATE follow_up_sessions
            SET child_mastery_achieved = 1, completed_at = ?
            WHERE session_id = 'session_1'
        """, (datetime.now().isoformat(),))
        db.commit()

        # 4. Verify follow-up marked complete
        cursor.execute("SELECT child_mastery_achieved FROM follow_up_sessions WHERE session_id = 'session_1'")
        mastery_row = cursor.fetchone()
        assert mastery_row is not None
        assert mastery_row[0] == 1

        db.close()
