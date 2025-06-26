from . import Kubectl
from models.response import MCPResponse
import requests

class Services(Kubectl):

	def __init__(self):
		super().__init__()

	async def get_services(self, options="-A") -> MCPResponse:
		cmd = ["kubectl", "get", "svc"] + self.default_options + options.split()
		return await self._get(cmd)

	async def set_selector(self, name: str, options: str) -> MCPResponse:
		cmd = ["kubectl", "set", "selector", "svc", name] + self.default_options + options.split()
		return await self._get(cmd)

	async def health_check(self, url: str) -> MCPResponse:
		try:
			res = requests.get(url)
			return MCPResponse(
				result={
					'headers': res.headers,
					'status_code': res.status_code,
					'body': res.text
				}
			)
		except Exception as e:
			return MCPResponse(
				error=str(e)
			)
