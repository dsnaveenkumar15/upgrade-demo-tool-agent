# tool-agent (demo)

A deliberately outdated example for the Radar upgrade agent: an MCP client pinned to `mcp==1.30.0`. It calls
`ClientSession.get_server_capabilities` and builds a `CallToolRequest` by hand, both of which later major releases removed.
Not meant to run; there are no secrets or endpoints here.
