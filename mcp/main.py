import json
from mcp.server.fastmcp import FastMCP
from pods import Pods
from namespace import NameSpaces

mcp = FastMCP("k8s")

@mcp.tool()
async def get_pods(namespace=None) -> str:
	""" Get pods under supplied namesapce, otherwise get all pods
	
		Args:
		  namespace: namespace name
	"""
	pods = Pods(namespace)
	pods = await pods.get()
	return json.dumps(pods.model_dump())


@mcp.tool()
async def get_namespaces() -> str:
	""" Get all namespaces """

	namespaces = NameSpaces()
	namespaces = await namespaces.get()
	return json.dumps(namespaces.model_dump())

if __name__ == "__main__":
	print("[mcp.run]")
	mcp.run(transport='stdio')

