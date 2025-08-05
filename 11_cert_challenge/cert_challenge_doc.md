
## Problem
Software engineers new to system design struggle to digest complex technical books and materials, becoming overwhelmed by jargon and giving up on their learning journey despite investing in quality resources.

For junior and mid-level software engineers, this problem represents a significant career bottleneck that directly impacts their professional growth and earning potential. These engineers often recognize that system design knowledge is essential for senior roles and successful technical interviews at top-tier companies, yet the traditional learning path through dense textbooks like Alex Xu's creates an insurmountable barrier. When they encounter complex concepts like "consistent hashing," "load balancing strategies," or "distributed consensus algorithms" without proper scaffolding, they experience cognitive overload that transforms what should be an exciting learning experience into a frustrating struggle that erodes their confidence and motivation.

The financial and career implications are substantial - these engineers have often invested hundreds of dollars in books, courses, and materials only to abandon them within weeks due to the overwhelming complexity. More critically, their inability to master system design concepts limits their ability to contribute meaningfully to architectural discussions, blocks their promotion to senior roles, and significantly reduces their competitiveness in the job market where system design interviews are standard for positions paying $300K+ at major tech companies. This creates a vicious cycle where the very people who most need to learn system design are systematically excluded from accessing this knowledge in a digestible format.

## Solution
This problem can be solved with an LLM powered system design study tutor! 

The AI-powered System Design Tutor transforms dense textbook learning into an interactive conversation where students ask questions in plain English and receive instant, tailored explanations grounded in authoritative sources. Instead of struggling through complex paragraphs about "consistent hashing," students simply ask "Why use consistent hashing over regular hashing?" and get clear, step-by-step explanations with real-world examples, followed by suggested follow-up topics to explore.

The user experience feels like having an expert mentor available 24/7 - they type questions into a clean React interface, watch the AI search relevant materials and current industry trends, and receive explanations that build on their existing knowledge rather than assuming expertise. The tutor remembers their learning progression, suggests related concepts, and allows them to upload additional materials, creating a personalized learning companion that transforms overwhelmed beginners into confident system design practitioners ready for technical interviews and senior-level discussions.

The tech stack for AI tutor 

- LLM: gpt-4.1, chosen for its great reasoning capabilities and reliability in generating accurate, contextually aware responses for complex educational content.
- Embedding model: OpenAI's text-embedding-3-small, selected for its excellent balance of performance and cost effectiveness while maintaining compatibility with the OpenAI ecosystem for seamless integration.
- Orchestration: Langraph, selected for its powerful agent orchestration capabilities that enable complex multi step workflows and conditional logic needed for sophisticated RAG implementations.
- vector database: qdrant, chosen for its high performance vector similarity search capabilities and excellent scalability for handling large document collections with fast retrieval times.
- monitoring: LangSmith, chosen for its comprehensive tracing and debugging capabilities specifically designed for LangChain/LangGraph applications, providing deep insights into agent behavior and performance.
- evaluation: RAGAS, selected as the industry standard evaluation framework for RAG applications, providing comprehensive metrics essential for systematic improvement.
- UI: React, chosen for its robust component based architecture and extensive ecosystem that enables building responsive, interactive educational interfaces with real-time agent interactions.


I will use an agent to take user input, and decide what tools to call to get context (RAG or Tavily) or output response directly to user. The agentic reasoning will handle tool selection, determine when to combine multiple information sources, and synthesize coherent responses by understanding the context and information requirements of each query.



## Data sources and external APIs
**Data source**

Alex Xu's book (pdf) "System Design Interview" is used as the data source. This is one of the most popular study material used by our audience, containing comprehensive system design concepts, patterns, and best practices. This book is also mostly facts based, so it's ideal for LLM to retrieve relevant context and generate accurate answers. 

**Chunking strategy**
 
Recursive Character Text Splitter is used for chunking. It hierarchically splits text by trying different separators (paragraphs, sentences, words) to maintain semantic coherence. This strategy preserves logical text structure better than fixed size chunking, ensuring that related concepts stay together within chunks, which improves retrieval accuracy and context quality for technical content like system design concepts where maintaining conceptual relationships is crucial for accurate answers.

**External API**
When the RAG system cannot find relevant context in the book to answer user queries, the agent will use Tavily to browse the internet and fill knowledge gaps. It supplements internal knowledge with current industry trends, recent developments, and information not covered in the book.


## RAG Evaluation
| Metric | Score |
|--------|-------|
| Context Recall | 0.9000 |
| Context Precision | 0.7222 |
| Faithfulness | 0.7502 |
| Answer Relevancy | 0.8535 |

Observations:
Strong Information Retrieval (90% Context Recall): The system successfully identifies and retrieves most of the relevant information needed to answer user questions, indicating effective document indexing and similarity search
 
Good Answer Relevance (85.35%): Generated responses are generally on-topic and address what users are asking, showing effective query understanding and response generation
Critical Weakness:
 
 Poor Context Precision (72.22%): This is the most concerning metric, indicating the system retrieves too many irrelevant documents alongside relevant ones, creating noise that could confuse the LLM and reduce response quality
Moderate Concern:
 
Questionable Faithfulness (75.02%): The LLM occasionally generates information not fully supported by the retrieved context, suggesting either hallucination or insufficient grounding in source material
 
Overall Assessment:
The pipeline shows good foundational capability in finding and addressing relevant information, but suffers from a "retrieval precision problem" where it casts too wide a net and includes irrelevant context. This likely impacts both response quality and system efficiency.


## Advance Retrieval
- Cohere Rerank Model： This will significantly improve context precision by intelligently reranking initially retrieved documents to filter out irrelevant content while maintaining the high recall already achieved.

- Parent Document Retrieval： Retrieving smaller chunks for relevance matching but returning larger parent documents for generation will improve faithfulness by providing more complete context while maintaining retrieval accuracy.

- Hybrid Search (Semantic + Keyword): Combining vector similarity search with BM25 keyword matching will improve precision for technical system design terminology where exact term matches are crucial alongside semantic understanding.

## Assessing Performance
Applying cohere ContextualCompressionRetriever, we got the following result



| Metric | naive_retriever | contextual_retriever | Change | Improvement |
|--------|----------|---------|---------|-------------|
| Context Recall | 0.9000 | 0.8524 | -0.0476 | ❌ **-4.8%** |
| Context Precision | 0.7222 | 0.8667 | +0.1445 | ✅ **+20.0%** |
| Faithfulness | 0.7502 | 0.7876 | +0.0374 | ✅ **+5.0%** |
| Answer Relevancy | 0.8535 | 0.9462 | +0.0927 | ✅ **+10.9%** |



- **Context Precision: +20%** - The Cohere rerank is working! Much cleaner, more relevant retrievals
- **Answer Relevancy: +10.9%** - Responses are significantly more on-target
- **Faithfulness: +5%** - Slight improvement in grounding


- **Context Recall: -4.8%** - Small decrease in completeness, likely due to more selective retrieval

 The system is now retrieving fewer documents but they're much more relevant, resulting in better overall performance.



## Changes to make for the app for later half of the course
features
- generate quiz from content and evaluate student's answer. This will make the app more interactive and fun. 
- study mode: craft a prompt for the tutor so it uses more socratic Q&A format when talking to students, instead of just dumping knowledge. 
- show reference (book and chapter) underneath the answer, so students can read more on interesting topics. 
