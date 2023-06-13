import streamlit as st
from css_utilities import format_list_with_css, format_card_with_css

tasks = [
    "Equip trainers with adult learning principles and effective facilitation methods",
    "Review and finalize the 2022 KDHS questionnaires",
    "Familiarize trainers with the 2022 KDHS CAPI system",
    "Prepare and finalize materials for training of survey personnel (interviewers, supervisors and biomarker technicians)"
]


def training(tasks = tasks):
    format_card_with_css('Training')
    st.info(
        """:blue[
    A total of 45 trainers drawn from KNBS, MoH, other government departments and agencies, universities, 
    and development partners participated in the training of trainers. The training was supported by ICF and 
    was held from November 29 to December 3, 2021. The objectives of the training were to]:
    """)
    format_list_with_css(tasks)


