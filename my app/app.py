import streamlit as st
from streamlit_option_menu import option_menu
import Home, Project_Parameters, Decision_Factors_Scoring

st.set_page_config(page_title="Decision Support System")

class MultiApp:
    def __init__(self):
        self.apps = []

    def add_app(self, title, function):
        self.apps.append({
            "title": title,
            "function": function
        })

    def run(self):
        if 'page' not in st.session_state:
            st.session_state.page = 'Home'
        
        with st.sidebar:
            app = option_menu(
                menu_title="Decision tool",
                options=["Home", "Project Parameters", "Decision Factors Scoring"],
                default_index=0 if st.session_state.page == 'Home' else 1 if st.session_state.page == 'Project Parameters' else 2 if st.session_state.page == 'Decision Factors Scoring' else 0,  
            )
        st.session_state.page = app
        
        if st.session_state.page == "Home":
            Home.app()
        elif st.session_state.page == "Project Parameters":
            Project_Parameters.app()
        elif st.session_state.page == "Decision Factors Scoring":
            Decision_Factors_Scoring.app()

app = MultiApp()
app.run()
