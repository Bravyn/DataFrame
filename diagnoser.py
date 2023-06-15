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
from staff_training import staff_training_data
from fieldwork_logistics import logistics
from data_processing import data_processing
from findings2 import findings
st.warning("Site in active development.")


introduction()
objectives()
survey_implementation()
questionnaires()
show_measurements()
training()
pretest()
staff_training_data()
logistics()
data_processing()
findings()
