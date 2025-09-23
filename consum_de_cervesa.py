import streamlit as st
import altair as alt
import polars as pl


df = pl.DataFrame({
    'age': ['Seattle', 'Seattle', 'Seattle', 'New York', 'New York', 'New York', 'Chicago', 'Chicago', 'Chicago'],
    'population': ['Apr', 'Aug', 'Dec', 'Apr', 'Aug', 'Dec', 'Apr', 'Aug', 'Dec'],
    'liters': [0.2, 85.0, 95.0, 90.0, 4.13, 3.58, 3.62, 3.98, 2.56]
})



chart = alt.Chart(df).mark_bar().encode(
    x = "city",
    y = "average(precip)"
)


st.header("Weather")
st.altair_chart(chart)



df = pl.DataFrame({
    'alumne': ['Anna', 'Bernat', 'Carla', 'David'],
    'examen-1': [7, 4, 10, 6],
    'examen-2': [6, 8, 7, 9],
    'examen-3': [8, 7, 9, 8]
})

df = df.with_columns(
    pl.mean_horizontal([pl.col('examen-1'), pl.col('examen-2'), pl.col('examen-3')]).alias('mitjana')
)


chart = alt.Chart(df).mark_bar().encode(
    x="mitjana",
    y="alumne"
)

st.altair_chart(chart)