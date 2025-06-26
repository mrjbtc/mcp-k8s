import json
import asyncio
from server import mcp
from tools import *

async def list_tools():
	tools = await mcp.list_tools()
	print("[available tools]:")
	for tool in tools:
		print(tool.name)

async def list_resources():
	resources = await mcp.list_resources()
	print("[available resources]:")
	for resource in resources:
		print(resource.name, resource.uri)

if __name__ == "__main__":
	print("[mcp.run]")
	asyncio.run(list_tools())
	print("\n")
	asyncio.run(list_resources())
	mcp.run(transport='stdio')