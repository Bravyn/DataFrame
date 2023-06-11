import streamlit as st
import pandas as pd
#import stanza

#nlp = stanza.Pipeline(lang='en', processors='tokenize, sentiment')


def get_patient_data():
    st.title("Diagnoser")
    st.header("Let us know how you feel")
    name = st.text_input("What is your name?")
    st.caption(f"Nice to meet you: {name.capitalize()}!")
    #st.divider()
    st.text("How old are you")
    age = st.slider("Drag to select age",min_value=5,max_value= 120,step= 1)
    st.caption(f"Your age is : {age}")
    feeling = st.text_area("How are you feeling?")
    origin_data = st.radio("When did you start feeling this way", ["Today", "Other day"])

    if origin_data.lower() == 'today':
        time = st.time_input("What time did it start")
    else:
        time = st.date_input("Which day did it start")

    return [[name, age, feeling, time]]

data = get_patient_data()
df = pd.DataFrame(data, columns=['Name', 'Age', 'Feeling', 'Started On'])

def show_data(data):
    st.table(data=data)

if len(data) != 0:
    if st.button("Show Entered Data"):
       show_data(data=df)   



