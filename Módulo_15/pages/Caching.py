import streamlit as st
import pandas as pd


st.set_page_config(
    page_title="EBAC | Módulo 15 | Streamlit I | Exercício",
    # page_icon="https://ebaconline.com.br/favicon.ico",
    page_icon="https://raw.githubusercontent.com/RodzMoraes/curso-ebac/main/Media/favicon.ico",
    layout="centered",
    initial_sidebar_state="auto",
)


st.markdown('''
<img src="https://raw.githubusercontent.com/RodzMoraes/curso-ebac/main/Media/ebac_logo_black.png" alt="ebac-logo">

---

# **Profissão: Cientista de Dados**
### **Módulo 15** | Streamlit I | Exercício

Aluno [Rodrigo Moraes](https://www.linkedin.com/in/moraes-rodrigo/)<br>
Data: 7 de maio de 2023.

---
            ''', unsafe_allow_html=True)

st.markdown("# Caching ❄️")
st.sidebar.markdown("# Caching ❄️")

'---'


@st.cache_data  # 👈 Add the caching decorator
def load_data(url):
    df = pd.read_csv(url)  # 👈 Download the data
    return df


df = load_data(
    "https://github.com/plotly/datasets/raw/master/uber-rides-data1.csv")
st.dataframe(df)

st.button("Rerun")

'---'
