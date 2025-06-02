from k8s_client import Kubectl
from models import MCPResponse
from pydantic import BaseModel
import json

class NameSpace(BaseModel):
	name: str
	status: str

class NameSpaces(Kubectl):
	
	def __init__(self):
		super().__init__(["kubectl", "get", "ns", "-o", "json"])

	async def get(self) -> MCPResponse:
		res = await self.run()

		if res["error"] is not None:
			return MCPResponse(
				error=res["error"]
			)

		list_namespace = []
		namespace = json.loads(res["result"].stdout)

		for item in namespace["items"]:
			list_namespace.append(NameSpace(
				name=item["metadata"]["name"],
				status=item["status"]["phase"]
			))

		return MCPResponse(result=list_namespace)