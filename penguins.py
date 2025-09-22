import altair as alt
import streamlit as st
import vega_datasets



@st.cache_data
def load_data():
    return vega_datasets.data.penguins()


penguins = load_data()

st.header("Penguins")

if st.checkbox("Show raw data"):
    st.write(vega_datasets.data.penguins.url)
    st.write(penguins)