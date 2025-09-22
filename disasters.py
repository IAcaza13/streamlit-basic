import altair as alt
import streamlit as st
import pandas as pd


@st.cache_data
def load_data():
    return pd.read_csv('https://github.com/vega/vega-datasets/blob/main/data/disasters.csv')

disasters = load_data()

st.header("Disasters")

mpg = alt.Chart(disasters).mark_line(point=True).encode(
    alt.X('Year'),
    alt.Y('Entity')
)

st.altair_chart(mpg)