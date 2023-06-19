import streamlit as st
from login import login

def sidebar():
    st.sidebar.image('./logo.png', caption="@Bravyn", width=180)
    st.sidebar.header("Log In")
    #menu_option = st.sidebar.radio(":blue[Menu Options]",["Intoduction", "View Implementation", "Objectives"])
    if st.sidebar.button("Login"):
        login()