# AI Reporting Platform

# Overview

The AI Reporting Platform is a modular, LLM-powered system designed to act as a Virtual Data Analyst. It supports natural language queries, multi-database connectivity, and dynamic reporting with insights and visualizations.

## The system supports:

Natural language query input  
 Role-based access control (Executive vs Analyst)  
 Real-time multi-DB connectivity (SQL, NoSQL, files)  
 Semantic enrichment of schema via LLM \+ web search  
 Stepwise query planning, decomposition, and execution  
 Result analysis, visualization, formatting, and delivery  
 Full **metadata tracking**, error handling, and orchestration via LangGraph

## Features

Query planning and execution  
 Schema introspection and enrichment  
 Insight generation and visualization  
 React-based frontend integration

## Workflow Example (LangGraph)

1. User query → Role resolved → Context created
2. Query planned → Decomposed → Tools selected
3. DBs introspection → Knowledge graph built → Queries run
4. Intermediate results stored → Analyzed → Visualized
5. Results formatted for React → Dispatched to UI or external system
6. Metadata saved at every step

#

# Full Functional Modules

## Security & Context Management

- UserRoleResolverAgent
  - Predefind roles: Executive, Analyst
- RoleToEntityAccessAgent
  - Uses LLM to determine what entities/tables user should have access to
- GlobalExecutionContext
  - Stores all state (Mongo – Meta DB): user, DBs, metadata, result flow
  - Tracks session state, step index, chat linkage, outputs
- StepLocalState
  - Mongo – session_steps
  - Logs tool inputs/outputs, runtime, collection reference, errors
- TempStorage
  - Mongo – TempDB
  - Stores per-step results for reuse or inspection
- Chat Logs
  - Mongo – chat_logs
  - Full message history, session-linked

### For Security

Parametrized queries (no raw SQL execution)  
 ExecutionGuardrails \+ FallbackExecutorTool  
 Session TTLs \+ audit logging of every step

## Data Infrastructure & Schema Understanding

- Database ConnectorTool
  - Connects to various DBs (MySQL, Mongo, CSV, etc.),
  - It will use packages like SqlAlchemy or PyMongo tools internally
- DBIntrospectorTool
  - Extracts raw schema from DBs (tables, columns, relationships),
  - Using PyMongo or SqlAlchemy internally
- SemanticEnricherAgent
  - Uses LLM \+ web to infer table/column purpose
- UserNoteIntegratorTool
  - Adds user knowledge to schema,
  - for demo this information would be in JSON format
- KnowledgeGraphBuilderTool —
  - Builds a reusable knowledge graph for all data
  - for demo it would be build from JSON data, rather than neo4j sort of database

## Query Understanding & Planning

- QueryPlannerAgent
  - Converts user query into logical plan
  - May invoke DBIntrospectorTool, SemanticEnricherAgent, WebSearchTool
  - Behaves as a **mini orchestrator** (sub-agent)
- QueryGenerationModel
  - Converts plan into tool-based steps (ideally one DB/table per step)
  - Each step contains: intent_id, db_type, query, target_table, depends_on
- QueryExecutionToolSelector
  - Decides tools per step using logic/metadata
- IntentClassifierAgent
  - Detects if new user message is a continuation or new session
  - Determines need for reinitializing context
- ClarificationDetectorAgent
  - Checks if user clarification changes planning
  - If yes, triggers replan

## Query Execution & Orchestration

- QueryExecutionToolSelector
  - Routes each step to SQLTool, MongoTool, or future types
  - Can enforce role-based routing or tool constraints
- QueryExecutorTool
  - Executes step with timeout, error capture, parameterized safety
  - Passes output to TempStorageTool
- TempStorageTool
  - Writes step output to ai_reporting_temp (MongoDB)
  - Naming: temp\_{session_id}\_step\_{n}
  - Includes retrieval and cleanup logic
- FallbackExecutorTool
  - Handles retries, alternate tool selection
  - Re-routes unsafe or failed steps
  - May retry, replan, or prompt clarification
- ResultMetadataTracker
  - Captures metadata per step (tool, params, runtime, output, etc.)
- LangGraphFlowEngine
  - LangChain-based orchestrator for full flow
  - QueryPlanner → QueryGenerationModel → StepExecutor → (clarification/fallback loop) → InsightGenerator \+ VisualizationBuilder \+ Formatter
- ExecutionGuardrails
  - Pre-run filters for: SQL injection patterns, unsafe patterns, complexity, row limits

### Orchestration

- PlannerNode: Wraps QueryPlannerAgent \+ enrichment tools
- StepGeneratorNode: Runs QueryGenerationModel
- ExecutionNode Runs tool via selector \+ guardrails \+ temp storage
- ClarificationNode Handles replanning based on user reply
- OutputNode Runs insight/visual/chart generation \+ delivery

## Output Analysis & Delivery

- InsightGeneratorAgent
  - Statistical analysis, summarization, correlation detection
  - Takes final query result \+ original query
  - Produces bullet-point summary \+ narrative insights
- VisualizationBuilderModel
  - Generates charts/tables from data
  - Converts insight to structured chart config (not image)
  - E.g: JSON: { "type": "bar", "xField": "city", "yField": "amount", "data": \[...\]}
- ReactFormatterAgent
  - Reads React component registry and formats data accordingly
  - Maps config to frontend component registry
  - Adds layout, wrappers, JSX or JSON for rendering
- ActionDispatcherTool
  - Uses MCP concept
  - Sends output via email, webhook, UI, or stores in cloud

### Visualization Output

Primary: React UI with chat & visualization  
 Webhook / Email (via ActionDispatcherTool)  
 PDF/image fallback

## External Knowledge Integration

- WebSearchTool
  - Enriches context from public data
- ExternalAPILoaderTool
  - Dynamically loads external APIs for data augmentation

## Result Metadata (Audit Trail)

- Metadata attached to every step detailing execution steps with all required context for re-execution
- Stored in: query_metadata collection in MongoDB

## Externalized Prompts

All agent and tool prompts have been externalized to the `prompts/` folder for better maintainability. Each prompt is stored in a separate file, categorized by agent or tool. For example:

- `prompts/query_planner_agent.txt`: Contains the prompt for the `QueryPlannerAgent`.
- `prompts/insight_generator_agent.txt`: Contains the prompt for the `InsightGeneratorAgent`.

This allows for easier updates and version control of prompts.

# Architecture & Tech Stack

## Updates for Production Readiness

### Backend Enhancements

- **ExecutionGuardrails**: Enhanced with logging for validation failures and support for custom validation rules.
- **FallbackExecutorTool**: Improved with detailed logging and dynamic tool selection.
- **LangGraphFlowEngine**: Extended with nodes for clarification handling and output formatting.
- **TempStorage** and **StepLocalState**: Optimized with indexing and TTL for faster queries and automatic cleanup.
- **ResultMetadataTracker**: Enhanced with detailed execution metrics, error details, and batch retrieval capabilities.
- **VisualizationBuilderModel**: Added support for scatter and heatmap charts.
- **InsightGeneratorAgent**: Extended to include statistical analyses and actionable recommendations.
- **QueryPlannerAgent**: Supports user feedback loops for refining logical plans.
- **QueryExecutionToolSelector**: Considers execution constraints for tool selection.

### Security Enhancements

- **Role-Based Access Control**: Enforced stricter validation of user roles against predefined permissions.
- **Session TTLs**: Added automatic expiration of inactive sessions.

### Frontend Enhancements

- **React Query**: Integrated for state management and API caching.
- **Error Boundaries**: Implemented to handle unexpected errors gracefully.
- **Health Checks**: Added to the frontend Dockerfile and Docker Compose configuration.

### Infrastructure Improvements

- **Docker**: Multi-stage builds added to backend and frontend Dockerfiles to optimize image size.
- **Docker Compose**: Health checks configured for backend, frontend, and MongoDB services.
- **CI/CD Pipeline**: Enforced test coverage thresholds for both backend and frontend.

### Testing

- Comprehensive unit tests added for all new components:
  - `StepLocalState`
  - `TempStorage`
  - `KnowledgeGraphBuilderTool`
  - `IntentClassifierAgent`
  - `ClarificationDetectorAgent`
  - `UserNoteIntegratorTool`
- Test coverage thresholds set to 90% for both backend and frontend.

### Documentation

- Updated to reflect the final implementation and production-ready state of the project.

## Updated Workflow Example

1. User query → Role resolved → Context created
2. Query planned → Decomposed → Tools selected
3. DBs introspection → Knowledge graph built → Queries run
4. Intermediate results stored → Analyzed → Visualized
5. Results formatted for React → Dispatched to UI or external system
6. Metadata saved at every step

## Deployment Notes

- Containerized using Docker (FastAPI backend, React frontend, MongoDB)
- Secured using OAuth for frontend \+ backend APIs
  - For demo version, APIs will be unsecured
- Scalable orchestration using LangGraph DAG nodes

## Tech Stack Summary

- **Frontend**: React \+ Material UI, component registry, responsive design
- **Backend**: FastAPI (async, modular), Pydantic, DI patterns
- **AI Layer**: LangGraph (DAG orchestrator), LangChain agents/tools
- **Containerization**: Docker \+ Docker Compose, .env config
  - Docker / Docker Compose / Azure Container Apps
- **Databases**: MongoDB (Meta \+ Temp, Qdrant (semantic store)
- **LLMs**: Configurable via YAML: Gemma, HuggingFace, OpenAI (using Langchain)
  - Tavily for Web Search
- **Client Databases**: Support for SQL Server, Mongo Db, CSV (uploaded to MongoDb)

## AI Agents & LangGraph

- Each agent must:
- Define expected input/output clearly
- Be mock-testable (no tight coupling with execution)
- Prompts must be externalized under prompts/
- LangGraph node functions must be:
- Deterministic and idempotent
- Retry-safe with state tracking

## Python (Backend \+ AI)

- Enforce type annotations via mypy
- Format with: black, isort, flake8, pylint
- Logging via loguru or similar structured logger

## React Frontend

- Use eslint, prettier, stylelint, typescript-eslint
- All linters must pass before merging to main
- Use React \+ TypeScript \+ Material UI
- State management: React Query or Zustand
- Component folder pattern:
- Use Zod/Yup for runtime schema validation
- Charts via Recharts or ECharts
- Test with @testing-library/react \+ jest

## Docker & Deployment

- Use Docker Compose for local orchestration
- Define services for:
- FastAPI, Mongo (Meta/Temp), SQL Server, Qdrant, LLM (Gemma/HuggingFace)
- Use .env, .env.dev, .env.prod
- Support hot reload with mounted volumes
- Add healthcheck blocks in docker-compose.yml

## CI/CD & Git Workflow

- Use GitHub Actions or GitLab CI:
- Steps: lint → test → coverage → docker build
- Git branches:
- main: production
- dev: integration
- Require:
- Tests \+ code review before merge
- Coverage thresholds enforced in CI

## Folder Structure

- `prompts/`: Contains externalized prompts for agents and tools.
- `backend/`: Backend services and logic.
- `frontend/`: React-based frontend.
- `infra/`: Deployment configurations.
- `docs/`: Documentation.

## Database Integration

The system supports both SQL and NoSQL databases. For SQL databases, SQLAlchemy is used for schema introspection and query execution. For NoSQL databases, PyMongo is used for MongoDB interactions.

### Installation Instructions

1. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

2. Ensure the following environment variables are set:
   - `SQLALCHEMY_DATABASE_URL`: Connection string for the SQL database.
   - `MONGO_URI`: Connection string for MongoDB.

### Testing

1. Run the test suite to verify database integration:

   ```bash
   pytest backend/tests/
   ```

2. Specific test cases for database interactions:
   - `test_query_executor_tool.py`: Tests query execution for both SQL and MongoDB.
   - `test_global_execution_context.py`: Tests session management and temporary storage in MongoDB.
