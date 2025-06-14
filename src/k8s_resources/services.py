from . import Kubectl
from models.response import MCPResponse
import json

class Services(Kubectl):

	def __init__(self):
		super().__init__()

	async def get_services(self, options="-A") -> MCPResponse:
		cmd = ["kubectl", "get", "svc"] + ["-o", "json"] + options.split()
		return self._get(cmd)
