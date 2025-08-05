# AI System Design Tutor - Certification Challenge

An AI-powered educational assistant that helps software engineers master system design concepts through interactive learning.

## Project Structure

📝 **`cert_challenge_doc.md`** - Written project documentation including problem analysis, solution design, tech stack choices, and evaluation results.

🔬 **`cert_challenge_experiment.ipynb`** - Jupyter notebook containing RAG pipeline experiments, retrieval method testing, and RAGAS evaluation implementation.

💻 **`system_design_agent_app/`** - Full-stack application code with:
- `api/` - FastAPI backend with LangGraph agent implementation
- `frontend/` - React UI for interactive chat interface
- `aimakerspace/` - Custom RAG utilities and vector database components

## Key Features

- **Intelligent Routing**: Agent decides between internal RAG search, external web search, or direct responses
- **Advanced Retrieval**: Cohere reranking for improved context precision (72% → 87%)
- **Real-time Learning**: Interactive chat interface with streaming responses

Built with LangGraph, OpenAI GPT-4, Qdrant, and React.
