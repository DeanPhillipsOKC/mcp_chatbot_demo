import streamlit as st
from modules.spinner import spinner_css

def configure_page():
    hide_streamlit_style = """
    <style>
      #MainMenu { visibility: hidden; }
      footer { visibility: hidden; }
      header { visibility: hidden; }
    </style>
    """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)
    st.markdown(spinner_css, unsafe_allow_html=True)  # Apply custom spinner CSS
    st.set_page_config(page_title="Payroll Assistant", layout="wide")
    st.title('How may I help you?')