from . import Kubectl
from models.response import MCPResponse
import json

class Deployments(Kubectl):

	def __init__(self):
		super().__init__()

	async def get_deployment(self, options="-A") -> MCPResponse:
		cmd = ["kubectl", "get", "deployment"] + ["-o", "json"] + options.split()
		return await self._get(cmd)

	async def describe_deployment(self, name: str, options="-A") -> MCPResponse:
		cmd = ["kubectl", "describe", "deployment", name] + ["-o", "json"] + options.split()
		return await self._get(cmd)

