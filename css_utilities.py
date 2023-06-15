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
                padding: 1rem;
                margin-bottom: .7rem;
                border-radius: .4rem;
                
                background-color: #f2f2f2;
                color: #000;
                background-color: rgba(255, 255, 255, 0.5);
                backdrop-filter: blur(.7rem);
                box-shadow: 0 0 .3rem rgba(0, 0, 0, 0.3);

            }}
        </style>
        """,
        unsafe_allow_html=True
    )

    for item in items:
        st.markdown(f'<div class="list-item">{item}</div>', unsafe_allow_html=True)



def format_card_with_css(item):
    
    st.markdown(
        f"""
        <style>
            .item {{
                padding: 1rem;
                margin-bottom: .7rem;
                border-radius: .4rem;
                background-color: #f2f2f2;
                color: #000;
                font-weight: bold;
                background-color: rgba(5, 255, 255, 0.2);
                backdrop-filter: blur(.7rem);
                box-shadow: 0 0 .8rem rgba(0, 0, 0, 0.3);

            }}
        </style>
        """,
        unsafe_allow_html=True
    )

    
    st.markdown(f'<div class="item">{item}</div>', unsafe_allow_html=True)

def format_list_with_css_blue(items):
    
    st.markdown(
        f"""
        <style>
            .list-item2 {{
                padding: 1rem;
                margin-bottom: .7rem;
                border-radius: .4rem;
                
                background-color: #f2f2f2;
                color: #008;
                background-color: rgba(255, 255, 255, 0.5);
                backdrop-filter: blur(.7rem);
                box-shadow: 0 0 .7rem rgba(0, 0, 0, 0.3);

            }}
        </style>
        """,
        unsafe_allow_html=True
    )

    for item in items:
        st.markdown(f'<div class="list-item2">{item}</div>', unsafe_allow_html=True)


def pretty_title(text):
    st.markdown(
        f"""
                <style>
                  .pretty_title{{
                      
                        background-color: #fff9;
                        border: 1px solid #000;
                        border-radius: 5px;
                        box-shadow: 0 2px 6px rgba(0, 0, 0, 0.1);
                        display: flex;
                        justify-content: center;
                        align-items: center;
                        cursor: pointer;
                        padding: 1.1rem;
                        margin: .3rem;  
                        font-size: 1rem;
                        font-weight: bold;
                      
                  }}
                </style>
                """, unsafe_allow_html=True)
    st.markdown(
        f"""
        <div class = "pretty_title">{text}></div>
        """, unsafe_allow_html=True
    )
    
    
    
       

