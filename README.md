### MCP server managing Kubernetes Cluster ###

## Claude Desktop ##

1. Create [kube-config](https://kubernetes.io/docs/concepts/configuration/organize-cluster-access-kubeconfig/) for accessing kubernetes API.
2. Build a docker image using Dockerfile.
`docker build . -t mcp:0.0.1`

3. Update the config `claude_desktop_config.json` with the following: 
```
{
  "mcpServers": {
    "k8s-mcp": {
       "command": "docker",
        "args": [
          "run",
          "--rm",
          "-i",
          "mcp:0.0.1",
          "uv",
          "run",
          "mcp/main.py"
        ]
    }
  }
}
```

4. Restart Claude desktop.