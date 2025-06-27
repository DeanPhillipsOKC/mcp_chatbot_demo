import streamlit as st
import pandas as pd
from modules.ui_helpers import _render_markdown_with_plots

def render_chat(chat_history):
    for m in chat_history:
        avatar = "images/pam-avatar.png" if m["role"] == "assistant" else "images/user-avatar.png"
        with st.chat_message(m["role"], avatar=avatar):
            if m["role"] == "assistant" and st.session_state.get("debug", False):
                rows = m.get("debug_rows", [])
                if rows:
                    df = pd.DataFrame(rows)
                    st.markdown("**🔧 Tool calls:**")
                    st.dataframe(df, use_container_width=True)
            if m["role"] == "assistant":
                _render_markdown_with_plots(m["content"])
            else:
                st.markdown(m["content"], unsafe_allow_html=True)