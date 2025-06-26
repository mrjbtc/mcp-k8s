import subprocess
import json
from models.response import MCPResponse
from typing import Dict, Any, Optional

class Kubectl():
	
	result = None

	default_options = ["-o", "json"]

	async def __run(self):

		if not self.cmd:
			return

		self.result = subprocess.run(
			self.cmd,
			stdout=subprocess.PIPE,
			stderr=subprocess.PIPE,
			text=True
		)

	async def _get(self, cmd=[]) -> MCPResponse:
		
		self.cmd = cmd
		await self.__run()

		if not self.result:
			return MCPResponse(
				error=f"""Error: empty result. @src/client/k8s_client.py. CMD: {self.cmd}"""
			) 

		if self.result.returncode != 0:
			return MCPResponse(
				error=f"""{self.result.stderr}"""
			)

		return MCPResponse(
			result=json.loads(self.result.stdout)
		)

