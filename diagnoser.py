"""This is a visualization of the Kenya Demographic
and Health Survey 2022 Key Indicators Report done 
by KNBS
This project was done by Ian Bravyns email:
ianbravynsa@gmail.com github username: @bravyn
Feel free to modify and improve as you wish
"""
import streamlit as st
import time
from sample_design import sample_design
from questionnaires import questionnaires


def survey_implementation():
    index = 1
    total_items = len(sample_design())

    st.subheader(":blue[SURVEY IMPLEMENTATION]")
    st.subheader(":violet[Sample Design]")
    for p in sample_design():
        st.info(p)


def colored_text(text):
    st.markdown(
            f"""
        <p style=
            "color: #000066;\
            line-height: 1.618rem;\
            text-style: underline;\
            text-align: center;">\
                {text}
        </p>
            """,
        unsafe_allow_html= True
        )


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
    st.subheader("Objectives")
    st.text("Primary Objective")
    colored_text(primary_objective)
    st.success("Specific Objectives")
    
    
    for index, objective in enumerate(objectives):
        st.write(objective)
        with st.expander(":blue[Click to view findings]"):
            st.write("This is more...")
        #time.sleep(.3)
        
    


def introduction():
    space_left, space_right , c= st.columns(3)
    with space_left:
        st.caption("Created by Ian Bravyn :sunglasses: (ianbravynsa@gmail.com)")
    with space_right:
        st.title(":violet[2022 Kenya Demographic and Health Survey]")
        st.caption("The pursuit of knowledge is a collaborative endeavor.")

    with c:
        st.empty()
    col1, col2 = st.columns(2)
    
    with col1:

        st.markdown(
            """
        <p style=
            "color: #000066;\
            letter-spacing: .618em;\
            line-height: 1.618rem;\
            text-style: underline;\
            text-align: center;">\
                Survey Details
        </p>
            """,
        unsafe_allow_html= True
        )
        
        st.markdown("- It is the seventh in Kenya. ")
        st.markdown("- Implemented by Kenya National Bureau of Statistics (KNBS)\
                    and Ministry of Health.")
        st.markdown("- Data collection took from February 17 to July 19, 2022.")
         
    with col2:

        st.markdown(
            """
        <p style=
            "color: #330000;\
            letter-spacing: .334rem;\
            line-height: 1.618rem;\
            text-align: center;">\
                Technical Assistance and Support
        </p>
            """,
        unsafe_allow_html= True
        )
        st.markdown("- Provided by the DHS Program\
                    funded by USAID")
        st.markdown(
            """
        <p style=
            "color: #000033;\
            letter-spacing: .1em;\
            text-align: center;">\
                Other Organizations offering Support
        </p>
            """,
        unsafe_allow_html= True
        )
        st.markdown("- Bill & Melinda Gates Foundation")
        st.markdown("- World Bank")
        st.markdown("- UNICEF")
        st.markdown(" - UNFPA")
        st.caption(" -And more")
def sidebar():
    st.sidebar.image('./logo.png', caption="@Bravyn", width=180)
    #st.sidebar.header("Menu")
    menu_option = st.sidebar.radio(":blue[Menu Options]",["Intoduction", "View Implementation", "Objectives"])
   
#sidebar()
introduction()
objectives()
survey_implementation()
questionnaires()
