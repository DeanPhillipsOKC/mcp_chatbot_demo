import streamlit as st

def initialize_session_state():
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []
    if "user_type" not in st.session_state:
        st.session_state.user_type = "Service"
    if "client_code" not in st.session_state:
        st.session_state.client_code = ""
    if "employee_email" not in st.session_state:
        st.session_state.employee_email = ""