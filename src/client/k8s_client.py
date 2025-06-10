import subprocess
import json
from models.response import MCPResponse
from typing import Dict, Any, Optional

class Kubectl():
	
	result = None

	def __init__(self, cmd=[]):
		self.cmd = cmd


	async def __run(self):
		self.result = subprocess.run(
			self.cmd,
			stdout=subprocess.PIPE,
			stderr=subprocess.PIPE,
			text=True
		)

	async def get(self) -> MCPResponse:

		await self.__run()
		if not self.result:
			return MCPResponse(
				error=f"""Error: empty result. @src/client/k8s_client.py"""
			) 

		if self.result.returncode != 0:
			return MCPResponse(
				error=f"""{self.result.stderr}"""
			)

		return MCPResponse(
			result=json.loads(self.result.stdout)
		)

