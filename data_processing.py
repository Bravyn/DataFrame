import streamlit as st
from css_utilities import format_card_with_css

def data_processing():
    format_card_with_css("DATA PROCESSING")
    with st.expander("""Computer-assisted personal interviewing (CAPI) was used during the 2022 KDHS data collection. The 
        devices used for CAPI were Android-based computer tablets programmed using a mobile version of 
        CSPro. :blue[Learn More.]
       
       """):
        st.caption("""
             The CSPro software was developed jointly by the U.S. Census Bureau, Serpro S.A., and The DHS 
Program. Programming of questionnaires into the Android application was done by ICF, while 
configuration of tablets was completed by KNBS in collaboration with ICF. All fieldwork personnel were 
assigned usernames, and devices were password protected to ensure the integrity of the data collected.
Work was assigned by supervisors and shared via Bluetooth® to interviewers’ tablets. Once completed,
assigned work was shared with supervisors, who did initial data consistency checks and edits and then 
submitted data to the central servers hosted at KNBS via SyncCloud. Data were downloaded from the 
central servers and checked against the inventory of expected returns to account for all data collected in the 
field. SyncCloud was also used to generate field check tables to monitor progress and flag any errors, 
which were communicated back to the field teams for correction.
Secondary editing was done by members of the central office team, who resolved any errors that were not 
corrected by field teams during data collection. A CSPro batch editing tool was used for cleaning and 
tabulation during data analysis.


        """)

