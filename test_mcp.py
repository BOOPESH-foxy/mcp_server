from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Boopesh-Profile")

@mcp.tool()
def get_name() -> str:
    """Returns the user's name."""
    return "Myself Boopesh"

@mcp.tool()
def get_work_info() -> str:
    """Returns current job details."""
    return "I'm currently working as PDE (Product Development Engineer) in RMCL"

@mcp.tool()
def get_location() -> str:
    """Returns residence information."""
    return "I reside in Tiruppur, Tamil Nadu"

if __name__ == "__main__":
    mcp.run(transport="stdio")