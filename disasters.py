import altair as alt
import streamlit as st
import vega_datasets
import pandas as pd


@st.cache_data
def load_data():
    github_csv_url = 'https://github.com/vega/vega-datasets/blob/main/data/disasters.csv'
    return pd.read_csv(github_csv_url)

disasters = load_data()

st.header("Disasters")

if st.checkbox("Show raw data"):
    st.write(vega_datasets.data.disasters.url)
    st.write(disasters)

mpg = alt.Chart(disasters).mark_line(point=True).encode(
    alt.X('Year'),
    alt.Y('Entity')
)

st.altair_chart(mpg)