import streamlit as st

def configure_sidebar():
    st.sidebar.image("images/pam.png", use_container_width=True)
    with st.sidebar.expander("🔒  Session settings", expanded=True):
        st.session_state.user_type = st.selectbox(
            "User type", ["Service", "Client", "Employee"],
            index=["Service", "Client", "Employee"].index(st.session_state.user_type)
        )
        if st.session_state.user_type == "Client":
            st.session_state.client_code = st.text_input(
                "Client code (required)", st.session_state.client_code
            )
            st.session_state.employee_email = ""
        elif st.session_state.user_type == "Employee":
            st.session_state.employee_email = st.text_input(
                "Email address (required)", st.session_state.employee_email
            )
            st.session_state.client_code = ""
        else:
            st.session_state.client_code = ""
            st.session_state.employee_email = ""
    with st.sidebar.expander("⚙️  Session controls", expanded=False):
        if st.button("🆕  New Chat", help="Clear history and start over"):
            st.session_state.chat_history = []
            st.rerun()
        st.checkbox("Debug", key="debug", help="Show debug statements")
    if st.session_state.user_type == "Client" and not st.session_state.client_code.strip():
        st.sidebar.warning("Client users must enter a client code before chatting.")
    if st.session_state.user_type == "Employee" and not st.session_state.employee_email.strip():
        st.sidebar.warning("Employee users must enter an email address before chatting.")