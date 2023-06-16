import streamlit as st
import pandas as pd
import numpy as np
from css_utilities import format_card_with_css, format_list_with_css_blue, format_list_with_css
data = {
    'Total Households': [42022],
    'Occupied Households': [38731],
    'Interviewed Households': [37911],
    'Eligible Women': [33879],
    'Interviewed Women': [32156],
    'Eligible Men': [16552],
    'Interviewed Men': [14453]
}

def findings():
    respondents = pd.DataFrame({"Women aged 15-19(%)": [19],"Men aged 15-19(%)":[23], "Men and women aged 45 -49(%)": [8]})
    marriage = pd.DataFrame({"Never married women(%)": [33], "Never Married men(%)": [48],
                             "Women either married or living with a man as if married(%)": [55],
                             "Married men / living as if married(%)": [46] })
    format_card_with_css("FINDINGS")
    format_list_with_css_blue([""" The proportion of both women and men respondents in the sample declines with increasing age, from 
19% of women and 23% of men in 15–19 age group to 8% of women and men in the 45–49 age group.
"""])
    st.write("The chart below represents response according\
             to age.")
    st.bar_chart(respondents)
    format_list_with_css_blue(["""
    About one-third of women (33%) and nearly half (48%) of men have never been married. Fifty-five 
    percent of women are either married or living together with a man as if married, while 46% of men are 
    married or living together with a woman as if married. """])
    st.write("The following chart shows responses on marriage")
    st.bar_chart(marriage)
    for i in data:
        st.info(i)
        format_list_with_css([data[i][0]])
    df = pd.DataFrame(data)
    st.dataframe(df)
    st.bar_chart(df)


