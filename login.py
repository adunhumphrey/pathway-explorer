import streamlit as st
import importlib
import base64

# Function to encode image to base64
def get_base64_image(image_path):
    with open(image_path, "rb") as image_file:
        encoded = base64.b64encode(image_file.read()).decode()
    return f"data:image/png;base64,{encoded}"  # Change format if needed (png, jpg, etc.)

USER_CREDENTIALS = {
    "humphrey": "password123@",
    "eoin": "E1on12@"
}

logo_image = get_base64_image("SBT_Logo.png")

def login():
    st.markdown(f"""
        <div style='text-align: center;'><img src="{logo_image}" width='300'></div>
    """, unsafe_allow_html=True)  # Add the logo at the top and center it
    st.markdown("<h1 style='font-family: Seaford; text-align: center;'>Login to Access the Dashboard</h1>", unsafe_allow_html=True)
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username in USER_CREDENTIALS and USER_CREDENTIALS[username] == password:
            st.session_state["authenticated"] = True
            st.success("Login successful!")
            st.rerun()
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