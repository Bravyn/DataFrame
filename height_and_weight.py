#anthropometric measurements
import streamlit as st
from css_utilities import format_list_with_css, format_card_with_css


measurements = [
    "Children under age 5",
    "Women age 15–49",
    "Men age 15–54"
]

def show_measurements(measurements = measurements):
    format_card_with_css("Anthropometric Measurements")
    st.info("Anthropometric(height/weight) measurements were conducted on: ")
    format_list_with_css(measurements)
    with st.expander(" Read more..."):
        st.caption(
            """
        Weight measurements were taken using Seca scales with a digital display (model SECA 874). Children 
        younger than age 24 months were measured lying down (recumbent length), while children older than 24 
        months and adults were measured standing (height). Height and length were measured with a Shorr 
        Board® measuring board.
        To assess the precision of measurements, two children were randomly selected in each cluster for 
        remeasurement. The 2022 KDHS adopted the guidelines of The DHS Program, which define a difference 
        of less than one centimeter between the two height measurements as an acceptable level of precision. The 
        data collection application was programmed to calculate anthropometric z scores automatically. Children 
        found to have a z score of less than negative three (−3) or more than three for height-for-age, weight-forheight, or weight-for-age were flagged as having unusual measurements and measured a second time. 
        Remeasurement of flagged cases was performed to ensure accurate reporting of height and weight 
        measurements. Children whose second measurement indicated severe wasting (weight-for-height z score 
        less than −3) were referred for treatment to the nearest health facility, and the field team supervisor or 
        another survey team member informed the caretaker of the affected child about the referral for treatment 
        before the team left the cluster
           """)
