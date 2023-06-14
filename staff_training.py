import streamlit as st
from css_utilities import format_card_with_css, format_list_with_css_blue

def staff_training_data():
    staff = 314
    supervisors = 48
    biomarker_technicians = 48
    female_interviewers = 144
    male_interviewers = 48
    reserves = 26
    training_period = "Jan 17 to February 13, 2022"
    combined =  [f'Total staff trained: {staff}', f'Supervisors:{supervisors}', f'Biomarker Technicians: {biomarker_technicians}',
            f'Female Interviewers: {female_interviewers}', f'Male Interviewers: {male_interviewers}',
            f'Reserves: {reserves}' ,f'Training Period: {training_period}']
    format_list_with_css_blue(combined)
    with st.expander("""The 
            training consisted of a detailed, question-by-question explanation of the questionnaires, accompanied by 
            explanations from the interviewer’s manual, role-play :blue[read more..]."""):
        st.caption("""
            The 
            training consisted of a detailed, question-by-question explanation of the questionnaires, accompanied by 
            explanations from the interviewer’s manual, role-play demonstrations, group discussions, in-class practice 
            interviewing in pairs and assessment tests.
            Anthropometry training provided all trainees with instruction, demonstrations, and practice in 
            length/height and weight measurements for children and adults. Trainees completed a standardization 
            7
            exercise involving measurements of children that was intended to gauge and improve accuracy and 
            precision. Restandardization exercises were conducted for those who did not pass the standardization 
            exercises.
        """)
