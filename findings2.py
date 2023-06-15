import streamlit as st
import pandas as pd
import numpy as np
from css_utilities import pretty_title
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
    
    pretty_title("FINDINGS")
    df = pd.DataFrame(data)
    st.dataframe(df)
    st.bar_chart(df)


