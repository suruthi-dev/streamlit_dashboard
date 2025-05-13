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

def interactive_plot(dataframe):
    x_axis_selection = st.selectbox("Select X-Axis", options=dataframe.columns)
    y_axis_selection = st.selectbox("Select Y-Axis", options=dataframe.columns)
    color = st.color_picker("Select a color to be applied in plot")

    plot = px.scatter(dataframe, x=x_axis_selection, y=y_axis_selection)
    plot.update_traces(marker=dict(color=color))
    st.plotly_chart(plot)

st.title("Hello Suru! ")
st.text("This is a webapp to explore data")

st.markdown('## This is a **Markdown**')

st.sidebar.title("Navigation")
uploaded_file = st.sidebar.file_uploader("Upload your file here! ")
options = st.sidebar.radio("Pages", options=["Home",'Data Statistics', "Data Header", "Scatter plot", "Interactive Plot" ])

if uploaded_file :
    df = pd.read_csv(uploaded_file)

    if options == 'Data Statistics':
        stats(df)
    elif options == "Data Header":
        header_df(df)
    elif options == "Scatter plot":
        scatter_plot(df)
    elif options == "Interactive Plot":
        interactive_plot(df)


else:
    st.text("Please Upload file to perform stat")













    # x_var = st.text_input("Enter X for scatterplot")
    # y_var = st.text_input("Enter Y for scatterplot")
