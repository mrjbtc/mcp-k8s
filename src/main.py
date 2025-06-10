import json
import asyncio
from server import mcp
from tools import get_deployments, get_namespaces, get_pods

async def list_tools():
	tools = await mcp.list_tools()
	print("[available tools]:")
	for tool in tools:
		print(tool.name)

if __name__ == "__main__":
	print("[mcp.run]")
	asyncio.run(list_tools())
	mcp.run(transport='stdio')

