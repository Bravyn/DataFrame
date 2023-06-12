import streamlit as st

questionnaires = [
    "Full Household Questionnaire",
    "Short Household Questionnaire",
    "Full Woman's Questionnaire",
    "Short Woman's Questionnaire",
    "Man's Questionnaire",
    "Full Biomarker Questionnaire",
    "Short Biomarker Questionnaire",
    "Fieldworker Questionnaire"
]

questionnaire_details = [
    {
        "name": "Full Household Questionnaire",
        "description": "Comprehensive questionnaire for household information",
    },
    {
        "name": "Short Household Questionnaire",
        "description": "Subset of questions from the full Household Questionnaire",
    },
    {
        "name": "Full Woman's Questionnaire",
        "description": "Detailed questionnaire for collecting information from women",
    },
    {
        "name": "Short Woman's Questionnaire",
        "description": "Subset of questions from the full Woman's Questionnaire",
    },
    {
        "name": "Man's Questionnaire",
        "description": "Questionnaire specifically designed for men",
    },
    {
        "name": "Full Biomarker Questionnaire",
        "description": "Questionnaire for collecting biomarker-related information",
    },
    {
        "name": "Short Biomarker Questionnaire",
        "description": "Subset of questions from the full Biomarker Questionnaire",
    },
    {
        "name": "Fieldworker Questionnaire",
        "description": "Questionnaire for fieldworkers involved in the survey",
    }
]

sample_division = {
    "full_questionnaire_sample": "Full Household, Woman's, and Man's Questionnaires",
    "short_questionnaire_sample": "Short Household and Woman's Questionnaires"
}

def questionnaires(questionnaires = questionnaires):
    st.subheader(":blue[Questionnaires]")
    st.success("The Household, Woman's, and Biomarker questionnaires \
            were divided into full and short versions \
            to reduce fieldwork length and interviewer/respondent fatigue.")
    for questionnair in questionnaires:
        with st.expander(questionnair):
            st.write("Hello")
