import asyncio
from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain_openai import ChatOpenAI
from langgraph.prebuilt import create_react_agent

async def create_mcp_agent():
    """Create an agent with MCP tools."""
    client = MultiServerMCPClient(
        {
            "mcp-server": {
                "command": "uv",
                "args": ["--directory", "/Users/chenshuzhou/workspace/AIE7-MCP-Session", "run", "server.py"],
                "transport": "stdio",
            },
        }
    )
    
    # Get tools from MCP server
    tools = await client.get_tools()

    # Create agent
    agent = create_react_agent("openai:gpt-4.1", tools)
    
    return agent

# Create the graph for LangGraph deployment
def create_graph():
    """Create the graph synchronously for LangGraph."""
    return asyncio.run(create_mcp_agent())

# Export the graph for LangGraph
graph = create_graph()