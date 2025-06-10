from . import Kubectl
import json

class Pods(Kubectl):

	def __init__(self, options="-A"):
		cmd = ["kubectl", "get", "pods"] + ["-o", "json"] + options.split()

		super().__init__(cmd)