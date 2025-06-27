# db_mcp_server.py
import oracledb
import os
import sys
from dotenv import load_dotenv
from fastmcp import FastMCP

load_dotenv(override=True)

mcp = FastMCP("OracleDB Tools")

def _check_service_user():
    """Check if the current user is a service user. Raise exception if not."""
    user_type = os.getenv("USER_TYPE", "Service")
    if user_type != "Service":
        raise PermissionError(f"Access denied: Only Service users can execute database queries. You are logged in as a {user_type} user. Please contact your administrator if you need database access.")

def _get_conn():
    _check_service_user()
    return oracledb.connect(
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASS"),
        dsn=os.getenv("DB_DSN")
    )

@mcp.tool()
def list_tables() -> str:
    print("🔧 list_tables called", file=sys.stderr)
    try:
        _check_service_user()
    except PermissionError:
        return "This feature is not allowed for employee self service users. If you believe you should have access, please contact your administrator."
    return """TABLE1: Description as to what it might be used for."""

@mcp.tool()
def describe_table(table: str) -> str:
    print(f"🔧 describe_table called with: {table}", file=sys.stderr)
    try:
        _check_service_user()
    except PermissionError:
        return "This feature is not allowed for employee self service users. If you believe you should have access, please contact your administrator."
    if table.upper() == "TABLE1":
        return """CLNT Table:
        - ID (NUMBER): The ID (primary key)"""
    return f"Table {table} not found."

@mcp.tool()
def run_sql(query: str) -> list[dict]:
    """
    Execute a read-only SQL query against the Oracle database and return the results as a list of dictionaries.

    The query must be a valid SELECT statement. If the query is not a SELECT statement,
    an error message will be returned instead.

    Do not put a trailling semicolon at the end of the query
    """
    print(f"🔧 run_sql called with: {query}", file=sys.stderr)
    try:
        _check_service_user()
    except PermissionError:
        return [{"error": "This feature is not allowed for employee self service users. If you believe you should have access, please contact your administrator."}]
    
    # if this is not a select query, return an error
    if not query.strip().lower().startswith("select"):
        return [{"error": "Only SELECT queries are allowed."}]

    # Log the query for debugging
    print(f"📤 Running SQL: {query}", file=sys.stderr)

    conn = _get_conn()
    cur = conn.cursor()
    cur.execute(query)
    cols = [d[0] for d in cur.description]
    rows = [dict(zip(cols, row)) for row in cur.fetchall()]
    cur.close()
    conn.close()
    return rows

# 🚨 THIS IS REQUIRED FOR MCP OVER STDIO TO WORK
if __name__ == "__main__":
    mcp.run(transport="stdio")
