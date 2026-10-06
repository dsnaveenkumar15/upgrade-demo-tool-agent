"""A command-line client that connects to a tool server over stdio and calls its tools, written for MCP 1.30."""
import asyncio

import mcp
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

SERVER = StdioServerParameters(command="python", args=["server.py"])


async def run(tool: str, arguments: dict) -> str:
    async with stdio_client(SERVER) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            capabilities = session.get_server_capabilities()
            if capabilities is None or capabilities.tools is None:
                raise RuntimeError("the server offers no tools")
            request = mcp.CallToolRequest(method="tools/call", params={"name": tool, "arguments": arguments})
            result = await session.send_request(request, mcp.CallToolResult)
            return "".join(part.text for part in result.content if getattr(part, "type", "") == "text")


if __name__ == "__main__":
    print(asyncio.run(run("add", {"a": 2, "b": 3})))
