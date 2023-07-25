import streamlit as st
import pandas as pd
import numpy as np
from datetime import date
from PIL import Image
import base64

st.set_page_config(page_title='Dashboard em Teste', layout = 'wide', page_icon = 'logo2.png', initial_sidebar_state = 'auto')
st.sidebar.image("https://i.imgur.com/SSWAdI4.png", use_column_width=True)

def page_home(): 
    st.markdown(
    """
    <style>
    section[data-testid="stSidebar"] 
    div[class="css-6qob1r eczjsme3"]
    {background-image: linear-gradient(#ffffff,#005545);color: white}
    </style>
    """,
    unsafe_allow_html=True)

def page_analitico():
    st.markdown(
    """
    <style>
    section[data-testid="stSidebar"] 
    div[class="css-6qob1r eczjsme3"]
    {background-image: linear-gradient(#ffffff,#005545);color: white}
    </style>
    """,
    unsafe_allow_html=True)
    dtinicial = st.sidebar.date_input("Data Inicial", format="DD/MM/YYYY")
    dtfinal = st.sidebar.date_input("Data Final", format= "DD/MM/YYYY")

    st.sidebar.write(dtinicial, " ~ ", dtfinal)

def page_backlog():
    st.markdown(
    """
    <style>
    section[data-testid="stSidebar"] 
    div[class="css-6qob1r eczjsme3"]
    {background-image: linear-gradient(#ffffff,#005545);color: white}
    </style>
    """,
    unsafe_allow_html=True)
    dtinicial = st.sidebar.date_input("Data Inicial", format="DD/MM/YYYY")
    dtfinal = st.sidebar.date_input("Data Final", format= "DD/MM/YYYY")

    st.sidebar.write(dtinicial, " ~ ", dtfinal)

def page_hxh():
    st.markdown(
    """
    <style>
    section[data-testid="stSidebar"] 
    div[class="css-6qob1r eczjsme3"]
    {background-image: linear-gradient(#ffffff,#005545);color: white}
    </style>
    """,
    unsafe_allow_html=True)
    dtinicial = st.sidebar.date_input("Data Inicial", format="DD/MM/YYYY")
    dtfinal = st.sidebar.date_input("Data Final", format= "DD/MM/YYYY")

    st.sidebar.write(dtinicial, " ~ ", dtfinal)

def page_csat():
    st.markdown(
    """
    <style>
    section[data-testid="stSidebar"] 
    div[class="css-6qob1r eczjsme3"]
    {background-image: linear-gradient(#ffffff,#005545);color: white}
    </style>
    """,
    unsafe_allow_html=True)
    dtinicial = st.sidebar.date_input("Data Inicial", format="DD/MM/YYYY")
    dtfinal = st.sidebar.date_input("Data Final", format= "DD/MM/YYYY")

    st.sidebar.write(dtinicial, " ~ ", dtfinal)

def main():
    st.sidebar.title("Menu")
    app_mode = st.sidebar.selectbox("",
                                    ["Página Inicial", "Analítico", "Hora x Hora", "Backlog", "CSAT"])

    if app_mode == "Página Inicial":
        page_home()
    elif app_mode == "Analítico":
        page_analitico()
    elif app_mode == "Hora x Hora":
        page_hxh()
    elif app_mode == "Backlog":
        page_backlog()
    elif app_mode == "CSAT":
        page_csat()

if __name__ == "__main__":
    main()