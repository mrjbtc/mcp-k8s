from . import Kubectl
from models.response import MCPResponse
import json

class Pods(Kubectl):

	def __init__(self):
		super().__init__()

	async def get_pods(self, options="-A") -> MCPResponse:
		cmd = ["kubectl", "get", "pods"] + ["-o", "json"] + options.split()
		return await self._get(cmd)

	async def describe_pods(self, name: str, options="-A") -> MCPResponse:
		cmd = ["kubectl", "describe", "pods", name] + ["-o", "json"] + options.split()
		return await self._get(cmd)
