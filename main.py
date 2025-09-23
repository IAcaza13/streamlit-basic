import streamlit as st


weather = st.Page("weather.py", title="Weather", icon=":material/add_circle:")
cars = st.Page("cars.py", title="Cars", icon=":material/add_circle:")
disasters = st.Page("disasters.py", title="Disasters", icon = ":material/add_circle:")
football =st.Page ("football.py", title="Football", icon = ":material/add_circle:")
consum_de_cervesa=st.Page("consum_de_cervesa.py", title="Consumer De's Cervesa", icon = ":material/add_circle:")
pg = st.navigation([weather,cars, disasters,football,consum_de_cervesa])
st.set_page_config(
    page_title="Altair | xtec.dev",
    page_icon="𝚾",
    initial_sidebar_state="expanded"
)

pg.run()