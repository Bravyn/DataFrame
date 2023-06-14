import streamlit as st
from sample_design import sample_design
from css_utilities import format_list_with_css, format_card_with_css
def survey_implementation():
    
    st.subheader(":blue[SURVEY IMPLEMENTATION]")
    format_card_with_css("Sample Design")

    paragrapghs = sample_design()
    for paragrapgh in paragrapghs:
        with st.expander(f"{paragrapgh[:108] } :blue[_Read More..._]"):
            format_list_with_css([paragrapgh])
    