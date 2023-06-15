import streamlit as st
from css_utilities import format_card_with_css

def logistics():
    format_card_with_css("FIELDWORK LOGISTICS")
    with st.expander("""Data collection for the 2022 KDHS was carried out by 48 teams from February 17 to July 13, 2022. Each 
team consisted of one supervisor, one biomarker technician, three female interviewers, one male 
interviewer, and a driver :blue[more..]"""):
        st.caption("""
            At the county level, the KDHS field teams were assisted by KNBS county 
statistical officers who provided links to national government administration officers (NGAOs). Prior to 
the data collection, a county mobilization team conducted targeted publicity within the clusters to prepare 
for the fieldwork. KNBS field staff and village elders assisted in identifying the sampled clusters and 
households. Monitoring of data collection was undertaken by Technical Working Committee and Steering 
Committee members throughout the data collection period. The aim of monitoring was to ensure that the 
survey was conducted according to the protocol and to provide real-time solutions to any challenges 
encountered.

        """)