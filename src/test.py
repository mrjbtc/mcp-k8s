import asyncio
import json
from k8s_resources import Services, Deployments, Pods, NameSpaces

async def get_k8s_resources():
    resource = Pods("-n dev-ai")
    resource = await resource.get()
    return json.dumps(resource.model_dump())

async def print_():
    o = await get_k8s_resources()
    print(o)


asyncio.run(print_())