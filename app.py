import os, sys, asyncio, traceback, textwrap, re
from pathlib import Path

import streamlit as st
import pandas as pd
from dotenv import load_dotenv

from modules.agent_manager import get_loop_and_agent
from modules.agent_runner import run_agent
from modules.ui_helpers import _render_markdown_with_plots
from modules.spinner import get_thinking_message, spinner_css
from modules.session_manager import initialize_session_state
from modules.sidebar_controls import configure_sidebar
from modules.chat_renderer import render_chat
from modules.page_config import configure_page
from modules.error_handler import handle_agent_error

load_dotenv(override=True)

# Page configuration
configure_page()

# Initialize session state
initialize_session_state()

# Sidebar controls
configure_sidebar()

# Initialize MCP servers and agent only once
if "loop" not in st.session_state or "agent" not in st.session_state:
    st.session_state.loop, st.session_state.agent = get_loop_and_agent(st.session_state.user_type)
LOOP = st.session_state.loop
AGENT = st.session_state.agent

# Chat input
user_msg = st.chat_input(
    "Ask a payroll-related question…",
    disabled=(
        (st.session_state.user_type == "Client" and not st.session_state.client_code.strip())
        or (st.session_state.user_type == "Employee" and not st.session_state.employee_email.strip())
    ),
)
if user_msg:
    st.session_state.chat_history.append({"role": "user", "content": user_msg})
    with st.spinner(get_thinking_message()):
        try:
            reply, debug_rows = run_agent(
                LOOP, AGENT,
                st.session_state.chat_history,
                user_msg,
                st.session_state.user_type,
                st.session_state.client_code,
                st.session_state.employee_email
            )
        except Exception as exc:
            reply, debug_rows = handle_agent_error(exc, st.session_state.user_type)
    if reply:
        st.session_state.chat_history.append({
            "role": "assistant",
            "content": reply,
            "debug_rows": debug_rows
        })

# Render conversation
render_chat(st.session_state.chat_history)
