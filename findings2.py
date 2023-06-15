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
#data2 = [f"{i} : {i[]} " for i in data]
def findings():
    
    format_card_with_css("FINDINGS")
    for i in data:
        st.info(i)
        format_list_with_css([data[i][0]])
    df = pd.DataFrame(data)
    st.dataframe(df)
    st.bar_chart(df)


