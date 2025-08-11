"""Toolbelt assembly for agents.

Collects third-party tools and local tools (like RAG) into a single list that
graphs can bind to their language models.
"""
from __future__ import annotations

import asyncio
from typing import List
from functools import lru_cache

from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_community.tools.arxiv.tool import ArxivQueryRun
from langchain_mcp_adapters.client import MultiServerMCPClient
from app.rag import retrieve_information


# Global variable to cache MCP tools
_mcp_tools_cache = None


async def _get_mcp_tools() -> List:
    """Async function to get tools from MCP server."""
    try:
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
        return tools
    except Exception as e:
        print(f"Warning: Could not connect to MCP server: {e}")
        return []


def _get_mcp_tools_sync() -> List:
    """Synchronous wrapper for getting MCP tools with caching."""
    global _mcp_tools_cache
    
    if _mcp_tools_cache is None:
        try:
            # Run the async function in a new event loop
            _mcp_tools_cache = asyncio.run(_get_mcp_tools())
        except Exception as e:
            print(f"Warning: Failed to get MCP tools: {e}")
            _mcp_tools_cache = []
    
    return _mcp_tools_cache


def get_tool_belt() -> List:
    """Return the list of tools available to agents (Tavily, Arxiv, RAG, MCP tools)."""
    # Standard tools
    tavily_tool = TavilySearchResults(max_results=5)
    standard_tools = [tavily_tool, ArxivQueryRun(), retrieve_information]
    
    # Try to get MCP tools
    mcp_tools = _get_mcp_tools_sync()
    
    return standard_tools + mcp_tools


def get_tool_belt_without_mcp() -> List:
    """Return the basic tool belt without MCP tools (fallback)."""
    tavily_tool = TavilySearchResults(max_results=5)
    return [tavily_tool, ArxivQueryRun(), retrieve_information]


