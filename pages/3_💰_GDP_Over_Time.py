import streamlit as st
import plotly.express as px

st.set_page_config(page_title="GDP Over Time", page_icon="💰", layout="wide")

st.markdown("# GDP Over Time")
st.sidebar.header("GDP Over Time")
st.write(
    """This visualization illustrates how GDP values have changed over time
    across the world. You can select specific countries and continents to examine, as
    well as specific year ranges."""
)

# -- Read in the data
df = px.data.gapminder()

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
        index=4,
    )

with country_col:
    all_countries = ["All"] + list(df["country"].unique())
    country_choice = st.multiselect(
        "What countries would you like to look at?",
        all_countries,
        default=["All"],
    )

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
    y="gdpPercap",
    color="country",
    hover_name="country",
    height=650,
)

fig.update_layout(title="GDP Per Capita by Year")
# -- Input the Plotly chart to the Streamlit interface
st.plotly_chart(fig, use_container_width=True)
