import plotly.express as px

# Line plot showing the trend of recovered cases over time in the US
fig1 = px.line(df_US, x="Date", y="Recovered", height=400, title="Recovered Cases Over Time in the US")
fig1.show()

# Line plot showing the trend of deaths over time in the US
fig2 = px.line(df_US, x="Date", y="Deaths", height=400, title="Deaths Over Time in the US")
fig2.show()

# Line plot showing the trend of confirmed cases over time in the US
fig3 = px.line(df_US, x="Date", y="Confirmed", height=400, title="Confirmed Cases Over Time in the US")
fig3.show()

# Line plot showing the trend of new daily cases over time in the US
fig4 = px.line(df_US, x="Date", y="New cases", height=400, title="New Cases Per Day in the US")
fig4.show()

import plotly.express as px

# ---------------- Active Cases Over Time ----------------
fig5 = px.line(
    df_US,
    x="Date",
    y="Active",
    height=400,
    title="Active COVID-19 Cases Over Time in the US"
)
fig5.show()

# ---------------- Daily Deaths Trend ----------------
fig6 = px.line(
    df_US,
    x="Date",
    y="New deaths",
    height=400,
    title="New Deaths Per Day in the US"
)
fig6.show()

# ---------------- 7-Day Rolling Average of New Cases ----------------
df_US["NewCases_7DayAvg"] = df_US["New cases"].rolling(window=7).mean()

fig7 = px.line(
    df_US,
    x="Date",
    y="NewCases_7DayAvg",
    height=400,
    title="7-Day Rolling Average of New COVID-19 Cases in the US"
)
fig7.show()

# ---------------- Recovery Rate Over Time ----------------
df_US["Recovery Rate"] = df_US["Recovered"] / df_US["Confirmed"]

fig8 = px.line(
    df_US,
    x="Date",
    y="Recovery Rate",
    height=400,
    title="COVID-19 Recovery Rate Over Time in the US"
)
fig8.show()

# ---------------- Death Rate Over Time ----------------
df_US["Death Rate"] = df_US["Deaths"] / df_US["Confirmed"]

fig9 = px.line(
    df_US,
    x="Date",
    y="Death Rate",
    height=400,
    title="COVID-19 Death Rate Over Time in the US"
)
fig9.show()
import plotly.express as px

# ---------------- Cumulative Cases vs Deaths ----------------
fig10 = px.line(
    df_US,
    x="Date",
    y=["Confirmed", "Deaths"],
    height=400,
    title="Cumulative Confirmed Cases vs Deaths in the US"
)
fig10.show()

# ---------------- Daily New Cases vs New Deaths ----------------
fig11 = px.line(
    df_US,
    x="Date",
    y=["New cases", "New deaths"],
    height=400,
    title="Daily New Cases vs New Deaths in the US"
)
fig11.show()

# ---------------- Active Cases vs Recovered ----------------
fig12 = px.line(
    df_US,
    x="Date",
    y=["Active", "Recovered"],
    height=400,
    title="Active Cases vs Recovered Cases Over Time in the US"
)
fig12.show()

# ---------------- Case Fatality Ratio Over Time ----------------
df_US["CFR"] = df_US["Deaths"] / df_US["Confirmed"] * 100  # Percentage

fig13 = px.line(
    df_US,
    x="Date",
    y="CFR",
    height=400,
    title="Case Fatality Ratio (%) Over Time in the US"
)
fig13.show()

# ---------------- Daily Growth Rate of Cases ----------------
df_US["DailyGrowthRate"] = df_US["Confirmed"].pct_change() * 100  # Percentage

fig14 = px.line(
    df_US,
    x="Date",
    y="DailyGrowthRate",
    height=400,
    title="Daily Growth Rate of COVID-19 Cases in the US (%)"
)
fig14.show()

# ---------------- Active Cases as % of Total Cases ----------------
df_US["ActivePercent"] = df_US["Active"] / df_US["Confirmed"] * 100

fig15 = px.line(
    df_US,
    x="Date",
    y="ActivePercent",
    height=400,
    title="Active Cases as Percentage of Total Confirmed Cases in the US"
)
fig15.show()
