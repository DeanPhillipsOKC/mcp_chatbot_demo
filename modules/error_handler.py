import streamlit as st

def handle_agent_error(exc, user_type):
    if "Access denied: Only Service users can execute database queries" in str(exc):
        reply = f"🚫 **Access Restricted**\n\nI'm sorry, but database queries can only be executed by Service users. You are currently logged in as a **{user_type}** user.\n\nIf you need to access database information, please:\n- Switch to a Service user account in the sidebar, or\n- Contact your system administrator for assistance\n\nI can still help you with other payroll-related questions that don't require direct database access."
        debug_rows = []
    elif ("permissionerror" in str(exc).lower() or "not allowed" in str(exc).lower() or "not permitted" in str(exc).lower()):
        reply = "🚫 **Feature Not Allowed**\n\nThis feature is not allowed for employee self service users. If you believe you should have access, please contact your administrator."
        debug_rows = []
    else:
        st.error(f"Agent error: {exc}")
        reply, debug_rows = None, []
    return reply, debug_rows