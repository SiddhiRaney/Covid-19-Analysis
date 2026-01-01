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
# ------------------- STEP 9: Line Charts for Trend Analysis -------------------

# 9️⃣ Line chart - Global confirmed cases trend over time
# Line charts are better for observing overall trends
fig8 = px.line(
    dataset2,
    x="Date",
    y="Confirmed",
    color="Country/Region",
    title="Confirmed Cases Trend Over Time (All Countries)",
    height=450
)
fig8.show()

# 10️⃣ Line chart - Deaths trend in USA
# Shows how deaths progressed with time in the US
fig9 = px.line(
    df_US,
    x="Date",
    y="Deaths",
    title="Death Cases Trend in USA",
    height=400
)
fig9.show()

# ------------------- STEP 10: Scatter Plot for Correlation Analysis -------------------

# 1️⃣1️⃣ Scatter plot - Confirmed vs Deaths (USA)
# Helps analyze correlation between confirmed cases and deaths
fig10 = px.scatter(
    df_US,
    x="Confirmed",
    y="Deaths",
    size="Confirmed",
    color="Deaths",
    title="Confirmed vs Deaths Correlation (USA)",
    height=450
)
fig10.show()

# ------------------- STEP 11: Area Chart for Cumulative Impact -------------------

# 1️⃣2️⃣ Area chart - Confirmed, Recovered, Deaths in USA
# Shows cumulative impact of covid over time
fig11 = px.area(
    df_US,
    x="Date",
    y=["Confirmed", "Recovered", "Deaths"],
    title="Cumulative COVID-19 Impact in USA",
    height=450
)
fig11.show()

# ------------------- STEP 12: Pie Chart for Distribution Analysis -------------------

# 1️⃣3️⃣ Pie chart - Distribution of cases on latest date (USA)
# Helps understand proportion of confirmed, recovered, and deaths
latest_date = df_US["Date"].max()
latest_data = df_US[df_US["Date"] == latest_date]

fig12 = px.pie(
    latest_data,
    values=[latest_data["Confirmed"].sum(),
            latest_data["Recovered"].sum(),
            latest_data["Deaths"].sum()],
    names=["Confirmed", "Recovered", "Deaths"],
    title="Case Distribution in USA (Latest Date)"
)
fig12.show()

# ------------------- STEP 13: Heatmap for Temporal Density -------------------

# 1️⃣4️⃣ Heatmap - Confirmed cases density over time (USA)
# Highlights periods of high infection density
fig13 = px.density_heatmap(
    df_US,
    x="Date",
    y="Confirmed",
    title="Confirmed Cases Density Over Time (USA)",
    height=450
)
fig13.show()
