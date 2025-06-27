import asyncio, os, sys, textwrap, atexit
from agents import Agent, Runner
from agents.mcp.server import MCPServerStdio
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent.resolve()
DB_SCRIPT = BASE_DIR / "mcp" / "db_mcp_server.py"
MOCKS_SCRIPT = BASE_DIR / "mcp" / "mocks_mcp_server.py"

def get_loop_and_agent(user_type):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    async def _startup():
        db_env = os.environ.copy()
        db_env["USER_TYPE"] = user_type

        db_server = MCPServerStdio(
            params={
                "command": sys.executable,
                "args": ["-u", str(DB_SCRIPT)],
                "env": db_env
            },
            cache_tools_list=True,
            client_session_timeout_seconds=10,
        )
        await db_server.__aenter__()
        await db_server.list_tools()

        mocks_server = MCPServerStdio(
            params={"command": sys.executable, "args": ["-u", str(MOCKS_SCRIPT)]},
            cache_tools_list=True,
            client_session_timeout_seconds=10,
        )
        await mocks_server.__aenter__()
        await mocks_server.list_tools()

        agent = Agent(
            name="PayrollAgent",
            instructions=textwrap.dedent("""
                You are PayrollAgent. Use the available database tools to
                answer payroll questions. Write queries in Oracle SQL.
                Never expose primary-key IDs unless explicitly asked.

                CHART CAPABILITIES:
                When users request charts or visualizations of database results:
                1. First, get the data using appropriate database tools
                2. Create interactive Plotly charts using ```plot``` code blocks
                3. Use go.Figure() for custom charts or px.* for quick charts
                4. Always include hover tooltips and professional styling
                5. Available chart types: bar, line, scatter, pie, histogram, box plots, etc.

                Example chart patterns:
                - Bar charts: go.Bar() with hovertemplate for detailed tooltips
                - Line charts: go.Scatter(mode='lines+markers') for trends
                - Pie charts: go.Pie() for breakdowns
                - Multiple series: Add multiple traces to same figure
                - Always end with: st.plotly_chart(fig, use_container_width=True)

                IMPORTANT: Employee users already provided their email in the header;
                never ask them again. Pass it automatically to any tool that needs it.

                WORKFLOW:
                1. When user requests action, use the appropriate tool
                2. After calling a tool, ALWAYS examine the tool's response 
                3. If tool returns success, create a confirmation message with details
                4. For chart requests, convert data to interactive Plotly visualizations
                5. ALWAYS end with "Final answer: [your complete response]"

                TOOL RESPONSE HANDLING:
                For tools that return structured responses with status and details:
                - Check if response has "status": "success"
                - If successful, create a professional confirmation table showing:
                  * A clear success header with checkmark
                  * All relevant details from the response in a formatted table
                  * The operation performed and its status
                - Use markdown tables for clean formatting
                - Include all important fields from the tool's response details
                - Make confirmations user-friendly and informative

                For database queries and informational tools:
                - Present results clearly and concisely
                - Use tables, lists, or charts as appropriate
                - Highlight key information the user requested
            """),
            mcp_servers=[db_server, mocks_server],
        )
        return db_server, mocks_server, agent

    db_server, mocks_server, agent = loop.run_until_complete(_startup())

    def _close():
        loop.run_until_complete(db_server.__aexit__(None, None, None))
        loop.run_until_complete(mocks_server.__aexit__(None, None, None))
        loop.stop()
    atexit.register(_close)

    return loop, agent