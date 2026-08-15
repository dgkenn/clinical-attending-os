# Action ↔ MCP tool map (maintainer reference)

Moved out of CUSTOM_GPT_INSTRUCTIONS.md — the GPT only ever sees the
operationIds it can call, so this table was pure token cost in every
conversation. Keep it current when the surfaces change.

## Action name ↔ Claude MCP tool name

ChatGPT calls these **Actions** (HTTP, via `openapi.json`); Claude calls the
same underlying Python functions as **MCP tools**. Both hit the identical
SQLite backend (`storage/sqlite/student_model.db`), so switching between
Claude and ChatGPT mid-campaign is safe — there is no separate state to drift
out of sync. Where the action's `operationId` differs from the MCP tool name
(a handful of older endpoints kept their original names), it's noted below.

| Action `operationId` | Claude MCP tool | HTTP route |
|

| Action `operationId` | Claude MCP tool | HTTP route |
---|---|---|
| `searchSources` | `search_clinical_sources` / `mcp_retrieval` | POST /search |
| `answer_from_clinical_sources` | `answer_from_clinical_sources` | POST /tutor |
| `start_study_session` | `start_study_session` | POST /start_session |
| `submit_study_answer` | `submit_study_answer` | POST /answer |
| `getDueReviews` | `get_due_reviews` | GET /due_reviews |
| `log_missed_topic` | `log_missed_topic` | POST /log_missed_topic |
| `submit_knowledge_points` | `submit_knowledge_points` | POST /knowledge_points/submit |
| `get_knowledge_points` | `get_knowledge_points` | GET /knowledge_points |
| `get_due_knowledge_points` | `get_due_knowledge_points` | GET /knowledge_points/due |
| `get_illness_script` | `get_illness_script` | GET /illness_script |
| `set_illness_script` | `set_illness_script` | POST /illness_script |
| `get_contrastive_case` | `get_contrastive_case` | GET /contrastive_case |
| `add_confusable_pair` | `add_confusable_pair` | POST /confusable_pair |
| `markMastered` | `mark_topic_mastered` | POST /mark_mastered |
| `get_session_state` | `get_session_state` | GET /session_state |
| `get_next_topic` | `get_next_topic` | GET /next_topic |
| `submit_answer` | `submit_answer` | POST /submit_answer_fsrs |
| `get_progress` | `get_progress` (medicine/ICU/anesthesia %) | GET /discipline_progress |
| `get_mastery_map` | `get_mastery_map` | GET /mastery_map |
| `set_medicine_weight` | `set_medicine_weight` | POST /medicine_weight |
| `get_dosing_drill` | `get_dosing_drill` | GET /dosing_drill |
| `submit_dosing_answer` | `submit_dosing_answer` | POST /dosing_drill/submit |
| `get_due_dosing_drills` | `get_due_dosing_drills` | GET /dosing_drill/due |
| `get_kp_to_study` | `get_kp_to_study` | GET /kp_to_study |
| `car_next` | `car_next` (same composite tool on both surfaces) | POST /car/next |
| `casePrep`, `startTeachingMode`, `followUp`, `getWeakPatterns` | (HTTP-only — no MCP equivalent; Claude reaches the same features through retrieval + its own session flow) | see relevant sections below |

