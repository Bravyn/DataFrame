import streamlit as st
from sample_design import sample_design

def survey_implementation():
    
    st.subheader(":blue[SURVEY IMPLEMENTATION]")
    st.subheader(":violet[Sample Design]")

    paragrapghs = sample_design()
    for paragrapgh in paragrapghs:
        with st.expander(f"{paragrapgh[:108] } :blue[_Read More..._]"):
            st.info(paragrapgh)
    