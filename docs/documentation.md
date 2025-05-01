# AI Reporting Platform

# Overview

The AI Reporting Platform is a modular, LLM-powered system designed to act as a Virtual Data Analyst. It supports natural language queries, multi-database connectivity, and dynamic reporting with insights and visualizations.

## The system supports:

 Natural language query input  
 Role-based access control (via Azure AD or internal DB)  
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

* UserRoleResolverAgent  
  * Resolves roles from Azure AD or internal DB  
* RoleToEntityAccessAgent  
  * Uses LLM to determine what entities/tables user should have access to  
* GlobalExecutionContext  
  * Stores all state (Mongo – Meta DB): user, DBs, metadata, result flow   
  * Tracks session state, step index, chat linkage, outputs  
* StepLocalState   
  * Mongo – session\_steps  
  * Logs tool inputs/outputs, runtime, collection reference, errors  
* TempStorage   
  * Mongo – TempDB  
  * Stores per-step results for reuse or inspection  
* Chat Logs   
  * Mongo – chat\_logs  
  * Full message history, session-linked

### For Security

 Parametrized queries (no raw SQL execution)  
 ExecutionGuardrails \+ FallbackExecutorTool  
 Session TTLs \+ audit logging of every step

## Data Infrastructure & Schema Understanding

* Databa	seConnectorTool  
  * Connects to various DBs (MySQL, Mongo, CSV, etc.),   
  * It will use packages like SqlAlchemy or PyMongo tools internally  
* DBIntrospectorTool  
  * Extracts raw schema from DBs (tables, columns, relationships),   
  * Using PyMongo or SqlAlchemy internally  
* SemanticEnricherAgent  
  * Uses LLM \+ web to infer table/column purpose  
* UserNoteIntegratorTool  
  * Adds user knowledge to schema,   
  * for demo this information would be in JSON format  
* KnowledgeGraphBuilderTool —   
  * Builds a reusable knowledge graph for all data   
  * for demo it would be build from JSON data, rather than neo4j sort of database

## Query Understanding & Planning

* QueryPlannerAgent  
  * Converts user query into logical plan  
  * May invoke DBIntrospectorTool, SemanticEnricherAgent, WebSearchTool  
  * Behaves as a **mini orchestrator** (sub-agent)  
* QueryGenerationModel  
  * Converts plan into tool-based steps (ideally one DB/table per step)  
  * Each step contains: intent\_id, db\_type, query, target\_table, depends\_on  
* QueryExecutionToolSelector  
  * Decides tools per step using logic/metadata  
* IntentClassifierAgent  
  * Detects if new user message is a continuation or new session  
  * Determines need for reinitializing context  
* ClarificationDetectorAgent  
  * Checks if user clarification changes planning  
  * If yes, triggers replan

## Query Execution & Orchestration

* QueryExecutionToolSelector  
  * Routes each step to SQLTool, MongoTool, or future types  
  * Can enforce role-based routing or tool constraints  
* QueryExecutorTool  
  * Executes step with timeout, error capture, parameterized safety  
  * Passes output to TempStorageTool  
* TempStorageTool  
  * Writes step output to ai\_reporting\_temp (MongoDB)  
  * Naming: temp\_{session\_id}\_step\_{n}  
  * Includes retrieval and cleanup logic  
* FallbackExecutorTool  
  * Handles retries, alternate tool selection  
  * Re-routes unsafe or failed steps  
  * May retry, replan, or prompt clarification  
* ResultMetadataTracker  
  * Captures metadata per step (tool, params, runtime, output, etc.)  
* LangGraphFlowEngine  
  * LangChain-based orchestrator for full flow  
  * QueryPlanner → QueryGenerationModel → StepExecutor → (clarification/fallback loop) → InsightGenerator \+ VisualizationBuilder \+ Formatter  
* ExecutionGuardrails  
  * Pre-run filters for: SQL injection patterns, unsafe patterns, complexity, row limits

### Orchestration

* PlannerNode: Wraps QueryPlannerAgent \+ enrichment tools  
* StepGeneratorNode: Runs QueryGenerationModel  
* ExecutionNode Runs tool via selector \+ guardrails \+ temp storage  
* ClarificationNode Handles replanning based on user reply  
* OutputNode Runs insight/visual/chart generation \+ delivery

## Output Analysis & Delivery

* InsightGeneratorAgent   
  * Statistical analysis, summarization, correlation detection  
  * Takes final query result \+ original query  
  * Produces bullet-point summary \+ narrative insights  
* VisualizationBuilderModel   
  * Generates charts/tables from data  
  * Converts insight to structured chart config (not image)  
  * E.g: JSON: {  "type": "bar", "xField": "city", "yField": "amount", "data": \[...\]}  
* ReactFormatterAgent   
  * Reads React component registry and formats data accordingly  
  * Maps config to frontend component registry  
  * Adds layout, wrappers, JSX or JSON for rendering  
* ActionDispatcherTool   
  * Uses MCP concept  
  * Sends output via email, webhook, UI, or stores in cloud

### Visualization Output

 Primary: React UI with chat & visualization  
 Webhook / Email (via ActionDispatcherTool)  
 PDF/image fallback

## External Knowledge Integration

* WebSearchTool   
  * Enriches context from public data  
* ExternalAPILoaderTool   
  * Dynamically loads external APIs for data augmentation

## Result Metadata (Audit Trail)

* Metadata attached to every step detailing execution steps with all required context for re-execution  
* Stored in: query\_metadata collection in MongoDB

# Architecture & Tech Stack

## Deployment Notes

* Containerized using Docker (FastAPI backend, React frontend, MongoDB)  
* Secured using OAuth for frontend \+ backend APIs  
  * For demo version, APIs will be unsecured  
* Scalable orchestration using LangGraph DAG nodes

## Tech Stack Summary

* **Frontend**: React \+ Material UI, component registry, responsive design  
* **Backend**: FastAPI (async, modular), Pydantic, DI patterns  
* **AI Layer**: LangGraph (DAG orchestrator), LangChain agents/tools  
* **Containerization**: Docker \+ Docker Compose, .env config  
  * Docker / Docker Compose / Azure Container Apps  
* **Databases**: MongoDB (Meta \+ Temp, Qdrant (semantic store)  
* **LLMs**: Configurable via YAML: Gemma, HuggingFace, OpenAI (using Langchain)  
  * Tavily for Web Search  
* **Client Databases**: Support for SQL Server, Mongo Db, CSV (uploaded to MongoDb)

## AI Agents & LangGraph

*  Each agent must:  
  *    Define expected input/output clearly  
  *    Be mock-testable (no tight coupling with execution)  
*  Prompts must be externalized under prompts/  
*  LangGraph node functions must be:  
  *    Deterministic and idempotent  
  *    Retry-safe with state tracking

## Python (Backend \+ AI)

*  Enforce type annotations via mypy  
*  Format with: black, isort, flake8, pylint  
*  Logging via loguru or similar structured logger

## React Frontend

* Use eslint, prettier, stylelint, typescript-eslint  
* All linters must pass before merging to main  
* Use React \+ TypeScript \+ Material UI  
* State management: React Query or Zustand  
* Component folder pattern:  
* Use Zod/Yup for runtime schema validation  
* Charts via Recharts or ECharts  
* Test with @testing-library/react \+ jest

## Docker & Deployment

*  Use Docker Compose for local orchestration  
*  Define services for:  
  *    FastAPI, Mongo (Meta/Temp), SQL Server, Qdrant, LLM (Gemma/HuggingFace)  
*  Use .env, .env.dev, .env.prod  
*  Support hot reload with mounted volumes  
*  Add healthcheck blocks in docker-compose.yml

## CI/CD & Git Workflow

*  Use GitHub Actions or GitLab CI:  
  *    Steps: lint → test → coverage → docker build  
*  Git branches:  
  *    main: production  
  *    dev: integration  
*  Require:  
  *    Tests \+ code review before merge  
  *    Coverage thresholds enforced in CI

## Folder Structure
- `backend/`: Backend services and logic.
- `frontend/`: React-based frontend.
- `infra/`: Deployment configurations.
- `docs/`: Documentation.
