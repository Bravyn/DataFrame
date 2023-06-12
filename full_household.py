
import streamlit as st

background_characteristics = [
    "Name",
    "Sex",
    "Age",
    "Education",
    "Relationship to the household head",
    "Survival of parents among children under age 18"
]

disability = [
    "Disability"
]

assets_land_housing = [
    "Assets",
    "Land ownership",
    "Housing characteristics"
]

sanitation_water_environment = [
    "Sanitation",
    "Water",
    "Other environmental health issues"
]

health_expenditures = [
    "Health expenditures"
]

accident_injury = [
    "Accident and injury"
]

covid19 = [
    "COVID-19 prevalence",
    "COVID-19 vaccination",
    "COVID-19 related deaths"
]

household_food_consumption = [
    "Household food consumption"
]

household_questionnaire = [
    background_characteristics,
    disability,
    assets_land_housing,
    sanitation_water_environment,
    health_expenditures,
    accident_injury,
    covid19,
    household_food_consumption
]

def display_questionnaire_items(household_questionnaire = household_questionnaire):
    for i, item in enumerate(household_questionnaire):
        col1, col2 = st.columns(2)
        with col1:
            st.write(f"Section { i + 1}")
            for j in item:
                st.text_input(j)
            

