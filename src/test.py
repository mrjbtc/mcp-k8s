import json
import asyncio
from k8s_resources import Services, Pods, Deployments, NameSpaces
from server import mcp

async def get_namespaces() -> str:
    namespaces = NameSpaces()
    namespaces = await namespaces.get_namespaces("-A")
    print(json.dumps(namespaces.model_dump()))

async def get_deployments() -> str:
    deployments = Deployments()
    deployments = await deployments.get_deployment("-A")
    print(json.dumps(deployments.model_dump()))


if __name__ == "__main__":
    asyncio.run(get_namespaces())
