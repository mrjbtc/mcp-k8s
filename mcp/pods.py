from k8s_client import Kubectl
from models import MCPResponse
from pydantic import BaseModel
import json

class Pod(BaseModel):
    name: str
    namespace: str

class Pods(Kubectl):

	def __init__(self, namespace=None):
		cmd = ["kubectl", "get", "pods", "-A", "-o", "json"]
		if namespace is not None:
			cmd = ["kubectl", "get", "pods", "-n", namespace, "-o", "json"]

		super().__init__(cmd)
	
	async def get(self) -> MCPResponse:
		res = await self.run()

		if res["error"] is not None:
			return MCPResponse(
				error=res["error"]
			)

		pods = json.loads(res["result"].stdout)
		list_pods = []
		for item in pods["items"]:
			list_pods.append(Pod(
				name=item["metadata"]["name"],
				namespace=item["metadata"]["namespace"]
			))
		return MCPResponse(result=list_pods)