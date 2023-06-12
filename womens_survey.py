import streamlit as st

socioeconomic_demographic_characteristics = [
    "Socioeconomic and demographic characteristics",
    "Reproduction",
    "Family planning",
    "Maternal health care and breastfeeding",
    "Vaccination and health of children",
    "Children’s nutrition",
    "Woman’s dietary diversity",
    "Early childhood development",
    "Marriage and sexual activity",
    "Fertility preferences",
    "Husbands’ background characteristics and women’s employment activity",
    "HIV/AIDS, other sexually transmitted infections (STIs), and tuberculosis (TB)",
    "Other health issues",
    "Early Childhood Development Index 2030",
    "Chronic diseases",
    "Female genital mutilation/cutting",
    "Domestic violence"
]

def display_womens_questionnaire(q = socioeconomic_demographic_characteristics):
    for i in q:
        st.write(f":blue[{i}]")

