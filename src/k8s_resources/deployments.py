from . import Kubectl
from models.response import MCPResponse
import json

class Deployments(Kubectl):

	def __init__(self):
		super().__init__()

	async def get_deployment(self, options="-A") -> MCPResponse:
		cmd = ["kubectl", "get", "deployment"] + self.default_options + options.split()
		return await self._get(cmd)

	async def describe_deployment(self, name: str, options="-A") -> MCPResponse:
		cmd = ["kubectl", "describe", "deployment", name] + self.default_options + options.split()
		return await self._get(cmd)

	async def set_image(self, name: str, image: str, tag: str, options: str) -> MCPResponse:
		cmd = ["kubectl", "set", "image", "deployment", name, f"""{name}={image}:{tag}"""] + self.default_options + options.split()
		return await self._get(cmd)

	async def scale_replicas(self, name: str, replicas: int, options: str) -> MCPResponse:
		cmd = ["kubectl", "scale", f"""--replicas={replicas}""", "deployment", name] + self.default_options + options.split()
		return await self._get(cmd)

	async def patch(self, name: str, namespace: str, options: str) -> MCPResponse:
		cmd = ["kubectl", "patch", "deployment", name, "-n", namespace, "--type=merge", "-p", options] + self.default_options 
		return await self._get(cmd)

