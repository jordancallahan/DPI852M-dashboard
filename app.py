import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(
    page_title="Real-Time Data Dashboard",
    layout="wide",
)

# -- Create three columns
col1, col2, col3 = st.columns([5, 5, 20])
with col3:
    st.title("DPI 852M Dashboard")
# The first column is a dummy to add a space to the left

# Get the user input
year_col, continent_col, log_x_col = st.columns([5, 5, 5])
with year_col:
    year_choice = st.slider(
        "What year would you like to examine?",
        min_value=1952,
        max_value=2007,
        step=5,
        value=2007,
        key="year",
    )
with continent_col:
    continent_choice = st.selectbox(
        "What continent would you like to look at?",
        ("All", "Asia", "Europe", "Africa", "Americas", "Oceania"),
        key="continent",
    )
with log_x_col:
    log_x_choice = st.checkbox("Log X Axis?")

# -- Read in the data
df = px.data.gapminder()
# -- Apply the year filter given by the user
filtered_df = df[(df.year == year_choice)]
# -- Apply the continent filter
if continent_choice != "All":
    filtered_df = filtered_df[filtered_df.continent == continent_choice]

# -- Create the figure in Plotly
fig = px.scatter(
    filtered_df,
    x="gdpPercap",
    y="lifeExp",
    size="pop",
    color="continent",
    hover_name="country",
    log_x=log_x_choice,
    size_max=60,
)
fig.update_layout(title="GDP per Capita vs. Life Expectancy")
# -- Input the Plotly chart to the Streamlit interface
st.plotly_chart(fig, use_container_width=True)

# Get the user input
year_col, continent_col, country_col = st.columns([5, 5, 5])
with year_col:
    year_choice = st.slider(
        "What year would you like to examine?",
        min_value=1952,
        max_value=2007,
        step=5,
        value=(1952, 2007),
    )
with continent_col:
    continent_choice = st.selectbox(
        "What continent would you like to look at?",
        ("All", "Asia", "Europe", "Africa", "Americas", "Oceania"),
    )

with country_col:
    all_countries = ["All"] + list(df["country"].unique())
    country_choice = st.multiselect(
        "What countries would you like to look at?",
        all_countries,
        default=["All"],
    )

# -- Read in the data
df = px.data.gapminder()
# Apply the year filter
filtered_df = df[(df.year >= year_choice[0]) & (df.year <= year_choice[1])]
# -- Apply the continent filter
if continent_choice != "All":
    filtered_df = filtered_df[filtered_df.continent == continent_choice]
# Apply the country filter
if "All" in country_choice:
    filtered_df = filtered_df
else:
    filtered_df = filtered_df[filtered_df.country.isin(country_choice)]


# -- Create the figure in Plotly
fig = px.line(
    filtered_df,
    x="year",
    y="lifeExp",
    color="country",
    hover_name="country",
)

fig.update_layout(title="Life Expectancy by Year")
# -- Input the Plotly chart to the Streamlit interface
st.plotly_chart(fig, use_container_width=True)


life_df = pd.read_csv("data/life_expectancy_years.csv")

st.write

# df = pd.read_csv("data/gdp_data.csv")

# df = df.rename(columns={"Country Name": "COUNTRY", "Country Code": "CODE"})
# df = df.drop([0, 1])
# df = df.drop(columns=["Indicator Name", "Indicator Code"])
# df = df.melt(id_vars=["COUNTRY", "CODE"], var_name="YEAR", value_name="GDP")
# df["GDP (BILLIONS)"] = df["GDP"].astype(float) / 1000000000

# fig = go.Figure(
#     data=go.Choropleth(
#         locations=df["CODE"],
#         z=df["GDP (BILLIONS)"],
#         text=df["COUNTRY"],
#         colorscale="Blues",
#         autocolorscale=False,
#         reversescale=True,
#         marker_line_color="darkgray",
#         marker_line_width=0.5,
#         colorbar_tickprefix="$",
#         colorbar_title="GDP<br>Billions US$",
#     )
# )

# st.plotly_chart(fig, use_container_width=True)
