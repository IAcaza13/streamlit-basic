import altair as alt
import streamlit as st
import vega_datasets



@st.cache_data
def load_data():
    return vega_datasets.data.football()


football = load_data()

st.header("football")

if st.checkbox("Show raw data"):
    st.write(vega_datasets.data.football.url)
    st.write(football)