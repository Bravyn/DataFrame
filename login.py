import streamlit as st
from css_utilities import format_list_with_css
def login():
    with st.form("Login"):
        #format_list_with_css(["Please Login"])
        st.write("Please Login")
        name = st.text_input("Email")
        password = st.text_input("Password")
        submit_button = st.form_submit_button("Submit")

    if submit_button:
        st.sidebar.error("Enter all setails")