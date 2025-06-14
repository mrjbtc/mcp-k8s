import json
from k8s_resources import Services
from server import mcp

@mcp.tool(
    annotations={
        "title": "Get services",
        "readOnlyHint": True,
        "destructiveHint": False,
        "openWorldHint": False
    }
)
async def get_services(options: str) -> str:
	""" Get services with additional options.
	
		Args:
		  options: string of options below
		    -A, --all-namespaces=false:
			If present, list the requested object(s) across all namespaces. Namespace in current context is ignored even
			if specified with --namespace.

		    --allow-missing-template-keys=true:
			If true, ignore any errors in templates when a field or map key is missing in the template. Only applies to
			golang and jsonpath output formats.

		    --chunk-size=500:
			Return large lists in chunks rather than all at once. Pass 0 to disable. This flag is beta and may change in
			the future.

		    --field-selector='':
			Selector (field query) to filter on, supports '=', '==', and '!='.(e.g. --field-selector
			key1=value1,key2=value2). The server only supports a limited number of field queries per type.

		    -f, --filename=[]:
			Filename, directory, or URL to files identifying the resource to get from a server.

		    --ignore-not-found=false:
			If the requested object does not exist the command will return exit code 0.

		    -k, --kustomize='':
			Process the kustomization directory. This flag can't be used together with -f or -R.

		    -L, --label-columns=[]:
			Accepts a comma separated list of labels that are going to be presented as columns. Names are case-sensitive.
			You can also use multiple flag options like -L label1 -L label2...

		    --no-headers=false:
			When using the default or custom-column output format, don't print headers (default print headers).

		    -o, --output='':
			Output format. One of: (json, yaml, name, go-template, go-template-file, template, templatefile, jsonpath,
			jsonpath-as-json, jsonpath-file, custom-columns, custom-columns-file, wide). See custom columns
			[https://kubernetes.io/docs/reference/kubectl/#custom-columns], golang template
			[http://golang.org/pkg/text/template/#pkg-overview] and jsonpath template
			[https://kubernetes.io/docs/reference/kubectl/jsonpath/].

		    --output-watch-events=false:
			Output watch event objects when --watch or --watch-only is used. Existing objects are output as initial ADDED
			events.

		    --raw='':
			Raw URI to request from the server.  Uses the transport specified by the kubeconfig file.

		    -R, --recursive=false:
			Process the directory used in -f, --filename recursively. Useful when you want to manage related manifests
			organized within the same directory.

		    -l, --selector='':
			Selector (label query) to filter on, supports '=', '==', and '!='.(e.g. -l key1=value1,key2=value2). Matching
			objects must satisfy all of the specified label constraints.

		    --server-print=true:
			If true, have the server return the appropriate table output. Supports extension APIs and CRDs.

		    --show-kind=false:
			If present, list the resource type for the requested object(s).

		    --show-labels=false:
			When printing, show all labels as the last column (default hide labels column)

		    --show-managed-fields=false:
			If true, keep the managedFields when printing objects in JSON or YAML format.

		    --sort-by='':
			If non-empty, sort list types using this field specification.  The field specification is expressed as a
			JSONPath expression (e.g. '{.metadata.name}'). The field in the API resource specified by this JSONPath
			expression must be an integer or a string.

		    --subresource='':
			If specified, gets the subresource of the requested object. This flag is beta and may change in the future.

		    --template='':
			Template string or path to template file to use when -o=go-template, -o=go-template-file. The template format
			is golang templates [http://golang.org/pkg/text/template/#pkg-overview].

		    -w, --watch=false:
			After listing/getting the requested object, watch for changes.

		    --watch-only=false:
			Watch for changes to the requested object(s), without listing/getting first.
	"""
	services = Services()
	services = await services.get_services(options)
	return json.dumps(services.model_dump())