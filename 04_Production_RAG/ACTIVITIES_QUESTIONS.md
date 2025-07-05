### LangGraph questions
##### ❓ Question #1:
What is the embedding dimension, given that we're using `text-embedding-3-small`?

##### ✅ Answer #1:
1536

#### ❓ Question #2:
LangGraph's graph-based approach lets us visualize and manage complex flows naturally. How could we extend our current implementation to handle edge cases? For example:
- What if the retriever finds no relevant context?  
- What if the response needs fact-checking?
Consider how you would modify the graph to handle these scenarios.

##### ✅ Answer #2:
- If the retriever finds no relevant context: we can create conditional edge after retrieve step. If no context, we can go to a new node that outputs "No relevant knoweldge found" and end the graph. If there is context, then we go to the "generate" node and output LLM reponse. 

- If the response needs fact-checking: we can add another node(fact-checking node) after generate, that will call LLM model to validate if the response is consistent with context provided, or use some external data source for validation, and output true or false. 


### LangSmith questions
#### ❓Question #1:

What conclusions can you draw about the above results?

Describe in your own words what the metrics are expressing.

##### ✅ Answer #1:


#### 🏗️ Activity #1:

Include a screenshot of your trace and explain what it means.

![LangSmith Trace](trace.png)




#### 🏗️ Activity #2:

Complete the prompt so that your RAG application answers queries based on the context provided, but *does not* answer queries if the context is unrelated to the query.

### answer: 
HUMAN_TEMPLATE = """
#CONTEXT:
{context}

QUERY:
{query}

Use the provide context to answer the provided user query. Only use the provided context to answer the query. If you do not know the answer, or if the query is unrelated to the provided context respond with "I don't know"
"""
