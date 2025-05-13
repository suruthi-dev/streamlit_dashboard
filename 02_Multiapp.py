import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

def stats(dataframe):
    st.header("Summary Statistics")
    st.write(dataframe.describe())

def header_df(dataframe):
    st.header("Data Header")
    st.write(df.head())

def scatter_plot(dataframe):
    fig,ax = plt.subplots(1,1)
    ax.scatter(x=dataframe['Insulin'], y=dataframe['Glucose'])
    ax.set_xlabel("Insulin")
    ax.set_ylabel("Glucose")
    st.pyplot(fig)


st.title("Hello Suru! ")
st.text("This is a webapp to explore data")

st.markdown('## This is a **Markdown**')

st.sidebar.title("Navigation")
uploaded_file = st.sidebar.file_uploader("Upload your file here! ")
options = st.sidebar.radio("Pages", options=["Home",'Data Statistics', "Data Header", "Scatter plot" ])

if uploaded_file :
    df = pd.read_csv(uploaded_file)

    if options == 'Data Statistics':
        stats(df)
    elif options == "Data Header":
        header_df(df)
    elif options == "Scatter plot":
        scatter_plot(df)


else:
    st.text("Please Upload file to perform stat")













    # x_var = st.text_input("Enter X for scatterplot")
    # y_var = st.text_input("Enter Y for scatterplot")
