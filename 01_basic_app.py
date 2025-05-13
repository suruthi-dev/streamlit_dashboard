import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px


st.title("Hello Suru! ")
st.text("This is a webapp to explore data")

st.markdown('## This is a **Markdown**')

uploaded_file = st.file_uploader("Upload your file here! ")

if uploaded_file :

    st.header("Data Statistics")
    df = pd.read_csv(uploaded_file)
    st.write(df.describe())

    st.header("Data Header")
    st.write(df.head())

    st.header("Scatter plot")
    fig,ax = plt.subplots(1,1)
    ax.scatter(x=df['Insulin'],y=df['Glucose'])
    ax.set_xlabel("Insulin")
    ax.set_ylabel("Glucose")

    st.pyplot(fig)
    



