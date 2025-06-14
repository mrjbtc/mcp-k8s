from . import Kubectl
from models.response import MCPResponse
import json

class NameSpaces(Kubectl):
	
	def __init__(self):
		super().__init__()

	async def get_namespaces(self, options="") -> MCPResponse:
		cmd = ["kubectl", "get", "ns"] + ["-o", "json"] + options.split()
		return await self._get(cmd)
