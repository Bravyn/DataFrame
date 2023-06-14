"""This is a visualization of the Kenya Demographic
and Health Survey 2022 Key Indicators Report done 
by KNBS
This project was done by Ian Bravyns email:
ianbravynsa@gmail.com github username: @bravyn
Feel free to modify and improve as you wish
"""
import streamlit as st
import time
from objectives import objectives
from questionnaires import questionnaires
from introduction import introduction
from survey_implementation import survey_implementation
from height_and_weight import show_measurements
from training import training
from pretest import pretest

st.warning("Site in active development.")


def sidebar():
    st.sidebar.image('./logo.png', caption="@Bravyn", width=180)
    #st.sidebar.header("Menu")
    menu_option = st.sidebar.radio(":blue[Menu Options]",["Intoduction", "View Implementation", "Objectives"])
   
#sidebar()
introduction()
objectives()
survey_implementation()
questionnaires()
show_measurements()
training()
pretest()