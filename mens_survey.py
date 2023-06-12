import streamlit as st

socioeconomic_demographic = [
    "Reproduction",
    "Family planning",
    "Marriage and sexual activity",
    "Fertility preferences",
    "Employment and gender roles",
    "HIV/AIDS, other STIs, and TB",
    "Other health issues",
    "Chronic diseases",
    "Female genital mutilation/cutting",
    "Domestic violence"
]


def display_mens_questionnaire(q = socioeconomic_demographic):
    for i in q:
        st.write(f":blue[{i}]")