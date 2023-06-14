import streamlit as st
from css_utilities import colored_text, format_list_with_css, format_card_with_css

def objectives():
    primary_objective = "The primary objective of the 2022 Kenya Demographic and Health Survey \
    (KDHS) is to provide current and comprehensive data on demographic, health,\
          and nutrition indicators. This data serves as a crucial guide for planning,\
              implementing, monitoring, and evaluating population and health-related \
                programs at both the national and county levels in Kenya."
    
    objectives = [
    "Estimate fertility levels and contraceptive prevalence",
    "Estimate childhood mortality",
    "Provide basic indicators of maternal and child health",
    "Estimate the Early Childhood Development Index (ECDI)",
    "Collect anthropometric measures for children, women, and men",
    "Collect information on children’s nutrition",
    "Collect information on women’s dietary diversity",
    "Obtain information on knowledge and behavior related to transmission of HIV and other sexually transmitted infections (STIs)",
    "Obtain information on noncommunicable diseases and other health issues",
    "Ascertain the extent and patterns of domestic violence and female genital mutilation/cutting"
]
    format_card_with_css("Objectives")
    st.info("Primary Objective")
    format_list_with_css([primary_objective])
    st.success("Specific Objectives")
    
    
    for index, objective in enumerate(objectives):
        st.write(objective)
        with st.expander(":blue[Click to view findings]"):
            st.write("This is more...")
        #time.sleep(.3)
        
  