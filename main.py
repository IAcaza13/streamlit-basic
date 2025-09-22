import streamlit as st


weather = st.Page("weather.py", title="Weather", icon=":material/add_circle:")
cars = st.Page("cars.py", title="Cars", icon=":material/add_circle:")
disasters = st.Page("disasters.py", title="Disasters", icon = ":material/add_circle:")
penguins =st.Page ("penguins.py", title="Penguins", icon = ":material/add_circle:")

pg = st.navigation([weather,cars, disasters,penguins])
st.set_page_config(
    page_title="Altair | xtec.dev",
    page_icon="𝚾",
    initial_sidebar_state="expanded"
)

pg.run()