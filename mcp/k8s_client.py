import subprocess

class Kubectl():
	
	def __init__(self, cmd=[]):
		self.cmd = cmd

	async def run(self):
		result = subprocess.run(
			self.cmd,
			stdout=subprocess.PIPE,
			stderr=subprocess.PIPE,
			text=True
		)

		res = {"error": None, "result": result}

		if result.returncode != 0:
			res["error"] = f"""Error: {result.stderr}"""

		return res
