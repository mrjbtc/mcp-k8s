from . import Kubectl
import json

class Deployments(Kubectl):

	def __init__(self, options="-A"):
		cmd = ["kubectl", "get", "deployment"] + ["-o", "json"] + options.split()

		super().__init__(cmd)