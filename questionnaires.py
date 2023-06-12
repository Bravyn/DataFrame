import streamlit as st
from full_household import display_questionnaire_items
from womens_survey import display_womens_questionnaire
from mens_survey import display_mens_questionnaire

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


def questionnaires(questionnaires = questionnaires):
    st.subheader(":blue[Questionnaires]")
    st.info("The Household, Woman's, and Biomarker questionnaires \
            were divided into full and short versions \
            to reduce fieldwork length and interviewer/respondent fatigue.")
    for i, questionnair in enumerate(questionnaires):
        with st.expander(questionnair):
            if i == 0:
                st.info(
                    """
                    The main purpose of the Household Questionnaire was to identify women and men who were eligible for 
                        individual interviews and women age 15–49, men age 15–54, and children age 0–59 months who were 
                        eligible for anthropometry. The Household Questionnaire collected information on:
                    """)
                
                display_questionnaire_items()

            elif i == 2:
                st.info(
                    """
                    The Woman’s Questionnaire was used to collect information from women age 15–49 on the following 
                    topics:
                    """)
                
                display_womens_questionnaire()
            elif i == 4:
                st.info(
                """
                The Man’s Questionnaire was administered to men age 15–54 living in the households selected for long 
                Household Questionnaires. The questionnaire collected information on:
                """)

                display_mens_questionnaire()
            else:
                st.info("Coming soon")