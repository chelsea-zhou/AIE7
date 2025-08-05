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

## Demo Video

🎥 **[Watch the Live Demo](https://www.loom.com/share/a9c665d57a9e49888915e9e8d8e02c02)** - See the AI System Design Tutor in action with real-time chat interactions and intelligent routing.
