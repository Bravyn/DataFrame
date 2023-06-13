import streamlit as st

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
import streamlit as st

def format_list_with_css(items):
    st.markdown(
        f"""
        <style>
            .list-item {{
                padding: 5px;
                margin-bottom: 5px;
                border-radius: 5px;
                background-color: #f2f2f2;
                color: #000;
                background: rgb(100,120,136);
            }}
        </style>
        """,
        unsafe_allow_html=True
    )

    for item in items:
        st.markdown(f'<div class="list-item">{item}</div>', unsafe_allow_html=True)


