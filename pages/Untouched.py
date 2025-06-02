import streamlit as st
import pandas as pd
import streamlit as st
import json

st.markdown(
    """
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Butterfly+Kids&family=Cabin:ital,wght@0,400..700;1,400..700&family=Mona+Sans:ital,wght@0,200..900;1,200..900&family=Noto+Serif:ital,wght@0,100..900;1,100..900&display=swap" rel="stylesheet">
    <style>
    *{
        border-radius: 0px;
        # background: #000000;
        font-family: 'Mona sans', arial;
    }
    h{
        font-family: 'Times New Roman', Times, serif;
        }
    table {
        border-collapse: collapse;
        width: 100%;
        table-layout: fixed;
    }
    th, td {
        border: 1px solid grey;
        color: white;
        background-color: #222222;
        padding: 8px;
        text-align: left;
        word-wrap: break-word;
    }
    th {
        background-color: #111111;
    }
    ::-webkit-scrollbar {
        display: none;
    }
    body {
        overflow: hidden;
    }
    p{
        font-family: 'Mona sans', arial;
        font-size: 23px !important;
        text-align: justify;
        }
    .font {
        font-family: 'Times New Roman', Times, serif;
        font-size: 50px !important;
        line-height: 1.6;
    }
    .para{
        font-family: 'Mona sans', arial;
        font-size: 16px;
    }
    .main{
        margin: 0px;
        padding: 0px;
        # padding: 0.5em;
        font-family: 'Mona sans' arial;
        # font-size: 16px;
        # display:flex;
        # flex-direction: column;
        background: #000000;
    }
    [data-testid="stSidebar"] {
        min-width: 20%;
        width: 20%;
        height: 100vh;
        position: sticky;
        top: 0;
        background-color: #000000;
        padding: 0px;
        color: white;
        # display: none;
        gap: 5px;
        *{
        border-radius: 0px;
        # margin: 0px;
        font-weight: normal;
        font-size: 23px;
        }
        border-right: 1px solid #555555;
        margin: 0px;
    }
    [data-testid="collapsedControl"] {
        visibility: hidden !important;
        display: none !important;
        color: #000000
        height: 0px;
        width: 0px;
        # border-radius: 0px;
    }
    .main-container {
        top: 0px;
        display: flex;
        flex-direction: row;
        # background: #000000;
    }
    #collapsedControl{
        visibility: hidden !important;
        display: none !important;
    }
    #MainMenu{
        visibility: hidden;
        }
    .stDeployButton {display:none;}
    header{visibility: hidden;}
    footer {visibility: hidden;}
    #stDecoration {display:none;}
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown('<p class="font">Untouched places.</p>', unsafe_allow_html=True)
st.text("")
st.text("")


st.title("Untraceable Monuments and Sites in India")

with open("./Resource/untraceable.json", "r", encoding="utf-8") as f:
    data = json.load(f)

df = pd.DataFrame(data)

df = df.reset_index(drop=True)

html_table = df.to_html(index=False)

st.markdown(html_table, unsafe_allow_html=True)