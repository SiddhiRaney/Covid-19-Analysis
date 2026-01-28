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


fig14 = px.bar(
    dataset2,
    x="Country/Region",
    y="Confirmed",
    color="Country/Region",
    animation_frame="Date",
    animation_group="Country/Region",
    title="Animated Growth of Confirmed Cases by Country",
    height=500
)
fig14.show()
# ------------------- STEP 14: Growth Rate Analysis -------------------

df_US = df_US.sort_values("Date")
df_US["New_Confirmed"] = df_US["Confirmed"].diff()

fig15 = px.line(
    df_US,
    x="Date",
    y="New_Confirmed",
    title="Daily New Confirmed Cases (USA)",
    height=450
)
fig15.show()

# ------------------- STEP 15: Rolling Average Trend -------------------

df_US["Confirmed_MA7"] = df_US["Confirmed"].rolling(7).mean()

fig16 = px.line(
    df_US,
    x="Date",
    y=["Confirmed", "Confirmed_MA7"],
    title="Confirmed Cases vs 7-Day Moving Average (USA)",
    height=450
)
fig16.show()

# ------------------- STEP 16: Box Plot for Distribution -------------------

fig17 = px.box(
    dataset2,
    x="Country/Region",
    y="Confirmed",
    title="Distribution of Confirmed Cases Across Countries",
    height=450
)
fig17.show()

# ------------------- STEP 17: Top-N Countries Comparison -------------------

latest_global = dataset2[dataset2["Date"] == dataset2["Date"].max()]
top10 = latest_global.groupby("Country/Region")["Confirmed"].sum().nlargest(10).reset_index()

fig18 = px.bar(
    top10,
    x="Country/Region",
    y="Confirmed",
    color="Confirmed",
    title="Top 10 Countries by Confirmed Cases",
    height=450
)
fig18.show()

# ------------------- STEP 18: Bubble Chart -------------------

fig19 = px.scatter(
    df_US,
    x="Confirmed",
    y="Recovered",
    size="Deaths",
    color="Deaths",
    title="Confirmed vs Recovered with Deaths as Bubble Size (USA)",
    height=450
)
fig19.show()

# ------------------- STEP 19: Facet Visualization -------------------

top_countries = top10["Country/Region"].tolist()
df_top = dataset2[dataset2["Country/Region"].isin(top_countries)]

fig20 = px.line(
    df_top,
    x="Date",
    y="Confirmed",
    facet_col="Country/Region",
    facet_col_wrap=3,
    title="Confirmed Cases Trend (Top 10 Countries)",
    height=600
)
fig20.show()

# ------------------- STEP 20: Choropleth Map (Global View) -------------------

fig21 = px.choropleth(
    latest_global,
    locations="Country/Region",
    locationmode="country names",
    color="Confirmed",
    title="Global COVID-19 Confirmed Cases (Latest Date)",
    height=500
)
fig21.show()

# ------------------- STEP 21: Correlation Heatmap -------------------

fig22 = px.imshow(
    df_US[["Confirmed", "Recovered", "Deaths"]].corr(),
    text_auto=True,
    title="Correlation Between COVID-19 Metrics (USA)",
    height=400
)
fig22.show()
# ------------------- STEP 22: Stacked Bar Chart -------------------

# Stacked bar - Confirmed, Recovered, Deaths (USA)
# Helps compare proportions over time
fig23 = px.bar(
    df_US,
    x="Date",
    y=["Confirmed", "Recovered", "Deaths"],
    title="Stacked COVID-19 Cases in USA Over Time",
    height=450
)
fig23.show()


# ------------------- STEP 23: Normalized (Percentage) Stacked Bar -------------------

# Shows percentage contribution of each metric
fig24 = px.bar(
    df_US,
    x="Date",
    y=["Confirmed", "Recovered", "Deaths"],
    title="Percentage Distribution of COVID-19 Metrics (USA)",
    height=450,
    barmode="stack"
)
fig24.update_layout(yaxis=dict(tickformat=".0%"))
fig24.show()


# ------------------- STEP 24: Time-Series with Range Slider -------------------

# Interactive range slider for long timelines
fig25 = px.line(
    df_US,
    x="Date",
    y="Confirmed",
    title="Confirmed Cases with Date Range Slider (USA)",
    height=450
)
fig25.update_xaxes(rangeslider_visible=True)
fig25.show()


# ------------------- STEP 25: Dual-Axis Line Chart -------------------

# Confirmed vs Deaths comparison using secondary axis
fig26 = px.line(
    df_US,
    x="Date",
    y=["Confirmed", "Deaths"],
    title="Confirmed vs Deaths Trend (USA)",
    height=450
)
fig26.show()


# ------------------- STEP 26: Histogram -------------------

# Distribution of daily confirmed cases
fig27 = px.histogram(
    df_US,
    x="New_Confirmed",
    nbins=50,
    title="Distribution of Daily New Confirmed Cases (USA)",
    height=450
)
fig27.show()


# ------------------- STEP 27: Violin Plot -------------------

# Distribution comparison using violin plot
fig28 = px.violin(
    dataset2,
    x="Country/Region",
    y="Confirmed",
    box=True,
    points="outliers",
    title="Confirmed Cases Distribution by Country",
    height=500
)
fig28.show()


# ------------------- STEP 28: Cumulative Sum Visualization -------------------

df_US["Cumulative_Deaths"] = df_US["Deaths"].cumsum()

fig29 = px.line(
    df_US,
    x="Date",
    y="Cumulative_Deaths",
    title="Cumulative Death Count Over Time (USA)",
    height=450
)
fig29.show()


# ------------------- STEP 29: Animated Line Chart -------------------

# Animated trend showing progression over time
fig30 = px.line(
    dataset2,
    x="Date",
    y="Confirmed",
    color="Country/Region",
    animation_frame="Date",
    title="Animated Confirmed Case Progression",
    height=500
)
fig30.show()


# ------------------- STEP 30: Sunburst Chart -------------------

# Hierarchical view of cases
fig31 = px.sunburst(
    latest_global,
    path=["Country/Region"],
    values="Confirmed",
    title="Hierarchical Distribution of Global Confirmed Cases",
    height=500
)
fig31.show()


# ------------------- STEP 31: Treemap -------------------

fig32 = px.treemap(
    latest_global,
    path=["Country/Region"],
    values="Confirmed",
    color="Confirmed",
    title="Treemap of Global COVID-19 Confirmed Cases",
    height=500
)
fig32.show()


# ------------------- STEP 32: Lag Analysis -------------------

# Lagging deaths by 7 days to observe delay effect
df_US["Deaths_Lag7"] = df_US["Deaths"].shift(7)

fig33 = px.scatter(
    df_US,
    x="Confirmed",
    y="Deaths_Lag7",
    title="Confirmed vs Deaths (7-Day Lag) - USA",
    height=450
)
fig33.show()


# ------------------- STEP 33: Rolling Growth Rate -------------------

df_US["Growth_Rate"] = df_US["New_Confirmed"].pct_change()

fig34 = px.line(
    df_US,
    x="Date",
    y="Growth_Rate",
    title="Daily Growth Rate of Confirmed Cases (USA)",
    height=450
)
fig34.show()
# ------------------- STEP 34: Weekly Aggregation -------------------

# Weekly confirmed cases (USA)
df_US["Week"] = df_US["Date"].dt.to_period("W").astype(str)
weekly_US = df_US.groupby("Week")[["Confirmed", "Deaths"]].sum().reset_index()

fig35 = px.line(
    weekly_US,
    x="Week",
    y=["Confirmed", "Deaths"],
    title="Weekly Confirmed vs Deaths (USA)",
    height=450
)
fig35.show()


# ------------------- STEP 35: Daily Recovery Rate -------------------

df_US["Recovery_Rate"] = df_US["Recovered"] / df_US["Confirmed"]

fig36 = px.line(
    df_US,
    x="Date",
    y="Recovery_Rate",
    title="Recovery Rate Over Time (USA)",
    height=450
)
fig36.show()


# ------------------- STEP 36: Mortality Rate -------------------

df_US["Mortality_Rate"] = df_US["Deaths"] / df_US["Confirmed"]

fig37 = px.line(
    df_US,
    x="Date",
    y="Mortality_Rate",
    title="Mortality Rate Trend (USA)",
    height=450
)
fig37.show()


# ------------------- STEP 37: Top 5 Countries Animated Line -------------------

top5 = top10.head(5)["Country/Region"].tolist()
df_top5 = dataset2[dataset2["Country/Region"].isin(top5)]

fig38 = px.line(
    df_top5,
    x="Date",
    y="Confirmed",
    color="Country/Region",
    animation_frame="Date",
    title="Animated Confirmed Cases (Top 5 Countries)",
    height=500
)
fig38.show()


# ------------------- STEP 38: Area Chart (Normalized) -------------------

fig39 = px.area(
    df_US,
    x="Date",
    y=["Confirmed", "Recovered", "Deaths"],
    title="Normalized COVID Metrics (USA)",
    height=450,
    groupnorm="percent"
)
fig39.show()


# ------------------- STEP 39: Scatter Matrix -------------------

fig40 = px.scatter_matrix(
    df_US,
    dimensions=["Confirmed", "Recovered", "Deaths"],
    title="Scatter Matrix of COVID Metrics (USA)",
    height=500
)
fig40.show()


# ------------------- STEP 40: Country-wise Growth Rate -------------------

dataset2 = dataset2.sort_values(["Country/Region", "Date"])
dataset2["Country_Growth"] = dataset2.groupby("Country/Region")["Confirmed"].pct_change()

fig41 = px.line(
    dataset2,
    x="Date",
    y="Country_Growth",
    color="Country/Region",
    title="Country-wise Growth Rate Over Time",
    height=500
)
fig41.show()


# ------------------- STEP 41: Cumulative Confirmed (Global) -------------------

dataset2["Global_Cumulative"] = dataset2.groupby("Country/Region")["Confirmed"].cumsum()

fig42 = px.line(
    dataset2,
    x="Date",
    y="Global_Cumulative",
    color="Country/Region",
    title="Cumulative Confirmed Cases by Country",
    height=500
)
fig42.show()


# ------------------- STEP 42: KDE Density Plot -------------------

fig43 = px.density_contour(
    df_US,
    x="Confirmed",
    y="Deaths",
    title="Density Contour of Confirmed vs Deaths (USA)",
    height=450
)
fig43.show()


# ------------------- STEP 43: Ranked Bar Chart -------------------

ranked = latest_global.sort_values("Confirmed", ascending=False)

fig44 = px.bar(
    ranked,
    x="Country/Region",
    y="Confirmed",
    title="Country Ranking by Confirmed Cases",
    height=500
)
fig44.show()


# ------------------- STEP 44: Log-Scale Line Comparison -------------------

fig45 = px.line(
    df_US,
    x="Date",
    y="Confirmed",
    log_y=True,
    title="Log-Scale Confirmed Case Trend (USA)",
    height=450
)
fig45.show()


# ------------------- STEP 45: Parallel Coordinates -------------------

fig46 = px.parallel_coordinates(
    df_US,
    dimensions=["Confirmed", "Recovered", "Deaths"],
    title="Parallel Coordinates of COVID Metrics (USA)",
    height=500
)
fig46.show()


# ------------------- STEP 46: Time-based Bubble Chart -------------------

fig47 = px.scatter(
    df_US,
    x="Date",
    y="Confirmed",
    size="Deaths",
    color="Recovered",
    title="Time-based Bubble Chart (USA)",
    height=500
)
fig47.show()


# ------------------- STEP 47: Daily Percentage Change -------------------

df_US["Daily_Percent_Change"] = df_US["Confirmed"].pct_change() * 100

fig48 = px.line(
    df_US,
    x="Date",
    y="Daily_Percent_Change",
    title="Daily Percentage Change in Confirmed Cases (USA)",
    height=450
)
fig48.show()


# ------------------- STEP 48: Rolling Standard Deviation -------------------

df_US["Confirmed_STD7"] = df_US["Confirmed"].rolling(7).std()

fig49 = px.line(
    df_US,
    x="Date",
    y="Confirmed_STD7",
    title="7-Day Rolling Std Dev of Confirmed Cases (USA)",
    height=450
)
fig49.show()
