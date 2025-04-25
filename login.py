import streamlit as st
import importlib

USER_CREDENTIALS = {
    "humphrey": "password123@",
    "eoin": "E1on12@",
    "sbti_user": "pathwayexplorer",
}

def login():
    st.title("Login to SBTi pathway explorer")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username in USER_CREDENTIALS and USER_CREDENTIALS[username] == password:
            st.session_state["authenticated"] = True
            st.success("Login successful!")
            st.rerun()()
        else:
            st.error("Invalid username or password!")

if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False

if not st.session_state["authenticated"]:
    login()
else:
    module_name = "app"
    if module_name:
        try:
            spec = importlib.util.spec_from_file_location(module_name, f"{module_name}.py")
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)  
        except Exception as e:
            st.error(f"⚠️ Error loading {module_name}: {e}")