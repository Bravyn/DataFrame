import streamlit as st
from css_utilities import format_card_with_css, format_list_with_css, format_list_with_css_blue

def introduction():
    space_left, space_right , c= st.columns(3)
    with space_left:
        st.caption("Created by Ian Bravyn :sunglasses: (ianbravynsa@gmail.com)")
    with space_right:
        st.title(":violet[The 2022 Kenya Demographic and Health Survey]")
        st.caption("The pursuit of knowledge is a collaborative endeavor.")

    with c:
        st.empty()
    col1, col2 = st.columns(2)
    
    with col1:

        format_card_with_css("Survey Details")
        format_list_with_css(['It is the seventh in Kenya.', 'Implemented by Kenya National Bureau of Statistics (KNBS)\
                    and Ministry of Health.', "Data collection took from February 17 to July 19, 2022."])
         
    with col2:
        format_card_with_css("Technical Support and Assistance")

        st.markdown(" Provided by the DHS Program and\
                    funded by USAID")
        format_list_with_css_blue(["Other Organizations offering Support"])
        st.markdown(" Bill & Melinda Gates Foundation")
        st.markdown(" World Bank")
        st.markdown(" UNICEF")
        st.markdown(" UNFPA")
        st.caption(" and more...")