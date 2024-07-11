import streamlit as st

def app():
    st.title("Home")
    st.write("Welcome to the Knowledge based decision support system for implementing digital twin in construction projects")
    st.write("This system will enable you to be able to access the extent to which digital twin is suitable to use for your project and will also guide you through the process of assessing your project and providing recommendations based on various factors. Click Next Button to proceed.")

    if st.button("Next"):
        st.session_state.page = 'Project Parameters'
        st.experimental_rerun()
