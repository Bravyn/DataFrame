import streamlit as st

def sidebar():
    st.sidebar.image('./logo.png', caption="@Bravyn", width=180)
    #st.sidebar.header("Menu")
    menu_option = st.sidebar.radio(":blue[Menu Options]",["Intoduction", "View Implementation", "Objectives"])
