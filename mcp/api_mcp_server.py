# api_mcp_server.py
import requests
from fastmcp import FastMCP

API_SPEC_URL = "https://api.example.com/openapi.json"

mcp = FastMCP("PayrollAPI Tools")

@mcp.tool()
def list_endpoints() -> list[str]:
    return list(requests.get(API_SPEC_URL).json().get("paths", {}).keys())

@mcp.tool()
def describe_endpoint(path: str) -> dict:
    return requests.get(API_SPEC_URL).json().get("paths", {}).get(path, {})
    
if __name__ == "__main__":
    mcp.run(transport="stdio")
