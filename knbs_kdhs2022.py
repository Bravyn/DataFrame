"""This is a visualization of the Kenya Demographic
and Health Survey 2022 Key Indicators Report done 
by KNBS
This project was done by Ian Bravyns email:
ianbravynsa@gmail.com github username: @bravyn
Feel free to modify and improve as you wish
"""
import streamlit as st

def introduction():
    space_left, space_right , c= st.columns(3)
    with space_left:
        st.caption("Created by Ian Bravyn(ianbravynsa@gmail.com)")
    with space_right:
        st.title("2022 Kenya Demographic and Health Survey")
    with c:
        st.caption("The pursuit of knowledge is a collaborative endeavor.")
    col1, col2 = st.columns(2)
    
    with col1:

        st.markdown(
            """
        <p style=
            "color: red;\
            letter-spacing: .618em;\
            line-height: 1.618rem;\
            text-align: center;">\
                Survey Details
        </p>
            """,
        unsafe_allow_html= True
        )
        
        st.markdown("- Conducted as the seventh in Kenya ")
        st.markdown("- Implemented by Kenya National Bureau of Statistics (KNBS)\
                    and Ministry of Health")
        st.markdown("- Data collection took from February 17 to July 19, 2022")
        #st.markdown("- ")
    
    
    with col2:

         st.markdown(
            """
        <p style=
            "color: red;\
            letter-spacing: .7em;\
            line-height: 2rem;\
            text-align: center;">\
                Technical Assistance and Support
        </p>
            """,
        unsafe_allow_html= True
        )


introduction()