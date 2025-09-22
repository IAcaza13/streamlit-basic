import altair as alt
import streamlit as st
import vega_datasets



@st.cache_data
def load_data():
    return vega_datasets.data.disaster()


disasters = load_data()

st.header("Disasters")

if st.checkbox("Show raw data"):
    st.write(vega_datasets.data.disasters.url)
    st.write(disasters)

mpg = alt.Chart(disasters).mark_line(point=True).encode(
    alt.X('Year'),
    alt.Y('entity')
)

st.altair_chart(mpg)