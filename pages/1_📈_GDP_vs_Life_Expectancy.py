import streamlit as st
import plotly.express as px
import time

st.set_page_config(
    page_title="GDP Per Capita vs Life Expectancy", page_icon="📈", layout="wide"
)

st.markdown("# DPI 852M Dashboard")
st.sidebar.header("GDP Per Capita vs Life Expectancy")
st.write(
    """This visualization illustrates the relationship between GDP per capita and life
    expectancy across the world.
    """
)

# -- Create two columns
col1, col2 = st.columns([5, 20])
with col2:
    st.title("GDP vs Life Expectancy")
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
    height=650,
)
fig.update_layout(title="GDP per Capita vs. Life Expectancy")
# -- Input the Plotly chart to the Streamlit interface
st.plotly_chart(fig, use_container_width=True)

progress_bar = st.sidebar.progress(0)
status_text = st.sidebar.empty()

for i in range(1, 101):
    status_text.text("%i%% Complete" % i)
    progress_bar.progress(i)

    time.sleep(0.05)

progress_bar.empty()

st.button("Re-run")
