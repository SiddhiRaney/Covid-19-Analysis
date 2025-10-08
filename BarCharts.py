# Advanced Data Visualization using Plotly Express

# Importing necessary library
import plotly.express as px

# ------------------- STEP 7: Advanced Data Visualization -------------------

# 1️⃣ Bar chart - Confirmed cases by date (all countries)
# Here we visualize how confirmed cases vary across different countries with time
fig1 = px.bar(
    dataset2,                     # dataset used (contains date column)
    x="Date",                     # x-axis shows the dates
    y="Confirmed",                # y-axis shows number of confirmed cases
    color="Confirmed",            # bar color intensity based on confirmed count
    hover_data=["Confirmed", "Date", "Country/Region"],  # tooltip info on hover
    height=400                    # height of the chart
)
fig1.show()

# 2️⃣ Bar chart with logarithmic scale for clearer trend visualization
# The log_y=True helps observe exponential growth trends more clearly
fig2 = px.bar(
    dataset2,
    x="Date",
    y="Confirmed",
    color="Confirmed",
    hover_data=["Confirmed", "Date", "Country/Region"],
    log_y=True,                   # logarithmic scale for y-axis
    height=400
)
fig2.show()

# 3️⃣ Bar chart - Death cases instead of confirmed
# Visualizing deaths by date for all countries
fig3 = px.bar(
    dataset2,
    x="Date",
    y="Deaths",                   # y-axis changed to 'Deaths'
    color="Deaths",               # color represents death count
    hover_data=["Confirmed", "Date", "Country/Region"], # hover details
    log_y=False,                  # linear scale for deaths
    height=400
)
fig3.show()

# ------------------- STEP 8: Country-Specific Visualization (USA Example) -------------------

# 4️⃣ Filtering dataset for United States only
# This helps in analyzing country-specific covid trends
df_US = dataset2.loc[dataset2["Country/Region"] == "US"]

# 5️⃣ Bar chart - Confirmed cases in USA
# Shows how confirmed cases increased over time
fig4 = px.bar(
    df_US,
    x="Date",
    y="Confirmed",
    color="Confirmed",
    height=400
)
fig4.show()

# 6️⃣ Bar chart - Recovered cases in USA
# Visualizes how recoveries progressed across time
fig5 = px.bar(
    df_US,
    x="Date",
    y="Recovered",
    color="Recovered",
    height=400
)
fig5.show()

# 7️⃣ Bar chart - Death cases in USA
# Displays death counts over time
fig6 = px.bar(
    df_US,
    x="Date",
    y="Deaths",
    color="Deaths",
    height=400
)
fig6.show()

# 8️⃣ Bar chart - Tests conducted in USA (if column exists)
# Helps analyze testing trends across the pandemic timeline
if "Tests" in df_US.columns:
    fig7 = px.bar(
        df_US,
        x="Date",
        y="Tests",
        color="Tests",
        height=400
    )
    fig7.show()
