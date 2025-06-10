from . import Kubectl
import json

class Services(Kubectl):

	def __init__(self, options="-A"):
		cmd = ["kubectl", "get", "svc"] + ["-o", "json"] + options.split()

		super().__init__(cmd)