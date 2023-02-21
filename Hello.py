import streamlit as st

st.set_page_config(
    page_title="DPI 852M Dashboard",
    page_icon="📊",
)

st.write("# DPI 852M Dashboard 📊")

st.sidebar.success("Select a visualization from the left.")

st.markdown(
    """
This is a dashboard that visualizes various global economic indicators, ranging from
GDP per capita, life expectancy, and others. The data is sourced from the
[Gapminder Foundation](https://www.gapminder.org/data/),
as well as the [World Bank](https://data.worldbank.org/).
"""
)
