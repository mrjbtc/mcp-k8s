from . import Kubectl
import json

class NameSpaces(Kubectl):
	
	def __init__(self, options=""):
		super().__init__(["kubectl", "get", "ns"] + ["-o", "json"] + options.split())
