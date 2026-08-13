# Claude Desktop MCP Server Configuration

## Overview

The Clinical Attending OS tutor system runs as a **Model Context Protocol (MCP) server** that integrates directly with Claude Desktop. This eliminates token overhead and enables real-time mastery tracking, retrieval-augmented tutoring, and adaptive follow-up learning.

## Prerequisites

1. **Claude Desktop** (macOS or Windows version)
2. **Python 3.10+** installed and in PATH
3. **MCP SDK**: Already in `requirements.txt` (run `pip install mcp` if needed)

## Setup Instructions

### Step 1: Locate Your Claude Desktop Config File

**macOS:**
```bash
~/Library/Application\ Support/Claude/claude_desktop_config.json
```

**Windows:**
```
%APPDATA%\Claude\claude_desktop_config.json
```

**Linux:**
```bash
~/.config/Claude/claude_desktop_config.json
```

### Step 2: Add the MCP Server Configuration

Open the config file and add the `clinical-attending` server to the `mcpServers` object:

```json
{
  "mcpServers": {
    "clinical-attending": {
      "command": "python",
      "args": ["-m", "src.mcp_server"],
      "cwd": "C:\\Users\\Dean\\anesthesia_attending"
    }
  }
}
```

**Important for Windows users:** Use double backslashes (`\\`) in the file path.

### Step 3: Restart Claude Desktop

Close and reopen Claude Desktop completely. The MCP server will start automatically.

### Step 4: Verify Setup

Ask Claude in a new conversation:

```
What tools do you have available?
```

You should see these 7 tools listed:

1. **mcp_retrieval** — Retrieve medical knowledge from the knowledge base
2. **get_session_state** — Get current student session state (due topics, weak areas, mastery)
3. **get_next_topic** — Get FSRS-prioritized next topic to study
4. **submit_answer** — Record student answer and update mastery tracking
5. **get_mastery_gates** — Check mastery status and phase advancement readiness
6. **get_progress** — Get overall progress statistics across curricula
7. **request_follow_up** — Request deeper learning on a subtopic during parent lesson

## Usage Examples

### Example 1: Start a Study Session

```
You: Let's study shock management.

Claude: [Calls get_session_state to check due topics]
         [Calls get_next_topic to select the next topic]
         [Calls mcp_retrieval with query="shock management"]

Claude responds with curated medical content from the knowledge base.
```

### Example 2: Submit an Answer and Update Mastery

```
You: Norepinephrine increases both afterload and inotropy.

Claude: [Evaluates answer]
         [Calls submit_answer with:
            topic="vasopressors"
            user_answer="Norepinephrine increases both afterload and inotropy"
            is_correct=true
            confidence_reported=4
            teach_back_quality=0.85
         ]

Claude responds: "Excellent! You've achieved baseline mastery on vasopressors..."
[FSRS scheduling updated automatically]
```

### Example 3: Request a Follow-Up Drill

```
You: I want to learn more about vasopressor dosing.

Claude: [Calls request_follow_up with:
           parent_topic="shock"
           requested_subtopic="vasopressor_dosing"
         ]

Claude enters nested session focusing on vasopressor dosing.
```

### Example 4: Check Progress

```
You: How am I doing overall?

Claude: [Calls get_progress]
         [Calls get_mastery_gates]

Claude responds with progress percentages and mastery levels.
```

## How It Works

```
┌─────────────────────┐
│ Claude Desktop      │
│                     │
│  User inputs        │
│  Conversation       │
└──────────┬──────────┘
           │
           │ MCP Protocol (stdio)
           │
┌──────────▼──────────┐
│ mcp_server.py       │
│ (MCP FastMCP)       │
│                     │
│ 7 Tools Registered: │
│  • mcp_retrieval    │
│  • session_state    │
│  • next_topic       │
│  • submit_answer    │
│  • mastery_gates    │
│  • progress         │
│  • follow_up        │
└──────────┬──────────┘
           │
           │ Python function calls
           │
┌──────────▼──────────┐
│ mcp_endpoints.py    │
│ (7 core functions)  │
└──────────┬──────────┘
           │
           │ Database queries + retrieval
           │
┌──────────▼──────────┐
│ SQLite DB +         │
│ Chroma Vector DB    │
│                     │
│ • Mastery tracking  │
│ • FSRS scheduling   │
│ • Follow-up state   │
│ • Knowledge base    │
└─────────────────────┘
```

## Features

✅ **Zero Token Overhead** — Tools don't consume prompt tokens like system prompts do  
✅ **Real-Time Mastery Tracking** — Automatic FSRS scheduling & mastery updates  
✅ **Adaptive Curriculum** — Next topic prioritized by FSRS, weak areas, and follow-ups  
✅ **Nested Learning** — Request deeper dives without losing context  
✅ **Persistent State** — Sessions resume automatically across conversations  
✅ **Confidence Weighting** — Interval adjustments based on reported confidence  
✅ **Local-First** — All data stored locally; no cloud calls required  

## Troubleshooting

### "Tool not found" Error

**Problem:** Claude says "mcp_retrieval tool not found"

**Solution:**
1. Restart Claude Desktop completely (not just the conversation)
2. Wait 3-5 seconds for the MCP server to initialize
3. Verify the config file path is correct
4. Check that `src/mcp_server.py` exists in the working directory

### Server Won't Start

**Problem:** "Connection refused" or "Python module not found"

**Solution:**
1. Verify Python is in PATH:
   ```bash
   python --version
   ```
   
2. Verify MCP SDK is installed:
   ```bash
   pip install mcp
   ```
   
3. Test server startup manually:
   ```bash
   cd C:\Users\Dean\anesthesia_attending
   python -m src.mcp_server
   ```
   
   You should see: `🎓 Clinical Attending OS — MCP Server running on stdio`

4. Press Ctrl+C to stop the test server

### Database Errors

**Problem:** "SQLite database is locked" or "Topic not found"

**Solution:**
1. Ensure the database file exists:
   ```bash
   ls -la data/student_db.sqlite
   ```
   
2. If missing, run the initialization script:
   ```bash
   python scripts/populate_phase1_knowledge.py
   ```

## Advanced Configuration

### Environment Variables

You can set environment variables in a `.env` file in the project root:

```env
DATABASE_PATH=data/student_db.sqlite
CHROMA_PATH=data/chroma_db
LOG_LEVEL=INFO
```

### Custom CWD

If you want to run the server from a different directory, adjust the `cwd` in the config:

```json
{
  "mcpServers": {
    "clinical-attending": {
      "command": "python",
      "args": ["-m", "src.mcp_server"],
      "cwd": "/path/to/anesthesia_attending"
    }
  }
}
```

### Logging

To enable debug logging, modify `src/mcp_server.py`:

```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

## Support

For issues or questions:

1. Check the [MCP Setup Guide](MCP_SETUP.md)
2. Review [MCP Endpoints Reference](MCP_ENDPOINTS.md)
3. Check server logs in the console

---

**Last Updated:** 2026-06-04  
**Status:** Production Ready
