import streamlit as st
from full_household import display_questionnaire_items
from womens_survey import display_womens_questionnaire
from mens_survey import display_mens_questionnaire
from css_utilities import format_card_with_css

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
    #st.subheader(":blue[Questionnaires]")
    format_card_with_css("Questionnaires")
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

            elif i == 1:
                st.info(
                    """
                The Selection of these subsamples was done 
                centrally at the head office—within a cluster, one in every two households was selected for the full 
                questionnaires, and the remaining households were selected for the short questionnaires. It is important to 
                note that the information collected in the short questionnaires were collected from all households and from 
                all women since these questionnaires were subsets of the full questionnaires
                """)
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
            elif i == 5 or i == 6:
                st.info(
                    """
                    The Biomarker Questionnaire collected information on anthropometry (weight and height). The long 
                    Biomarker Questionnaire collected anthropometry measurements for children age 0–59 months, women 
                    age 15–49, and men age 15–54, while the short questionnaire collected weight and height measurements 
                    only for children age 0–59 months.
                    """)
            elif i == 7:
                st.info(
                    """
                    The Fieldworker Questionnaire was used to collect basic background information on the people who 
                    collected data in the field. This included team supervisors, interviewers, and biomarker technicians
                    """)
            else:
                st.success("")
    st.caption(
                """
                All questionnaires except the Fieldworker Questionnaire were translated into the Swahili language to make 
                it easier for interviewers to ask questions in a language that respondents could understand. All
                questionnaires were programmed into tablet computers to allow for computer-assisted personal 
                interviewing (CAPI) for data collection purposes, with the capability to choose Swahili or English.
                The protocol for the 2022 KDHS was reviewed by the ICF Institutional Review Board.

                """)