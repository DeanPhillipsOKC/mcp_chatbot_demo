import re
import traceback
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import streamlit as st

def create_animated_thinking_message(message: str) -> str:
    """Convert a thinking message into animated HTML with bouncing letters"""
    words = message.split()
    animated_words = []

    for word in words:
        if len(word) > 3:  # Only animate longer words
            animated_chars = []
            for i, char in enumerate(word):
                if char.isalpha():
                    delay = i * 0.1
                    animated_chars.append(f'<span class="bouncing-text" style="animation-delay: {delay}s">{char}</span>')
                else:
                    animated_chars.append(char)
            animated_words.append(''.join(animated_chars))
        else:
            animated_words.append(word)

    return ' '.join(animated_words) + ' <span class="thinking-dots"></span>'

def _render_markdown_with_plots(content: str) -> None:
    # Handle None content gracefully
    if content is None:
        st.error("❌ No content to display")
        return

    pattern = re.compile(r"```plot\s*([\s\S]*?)```", re.MULTILINE)
    cursor = 0
    for match in pattern.finditer(content):
        before = content[cursor:match.start()]
        if before.strip():
            st.markdown(before, unsafe_allow_html=True)
        code = match.group(1).strip()
        try:
            # Create namespace with Plotly and Streamlit
            plot_globals = {
                "go": go, 
                "px": px, 
                "pd": pd,
                "st": st
            }
            exec(code, plot_globals)
        except Exception:
            st.error("❌ Plot error:\n```\n" + traceback.format_exc() + "\n```")
            cursor = match.end()
            continue
        cursor = match.end()
    remaining = content[cursor:]
    if remaining.strip():
        st.markdown(remaining, unsafe_allow_html=True)