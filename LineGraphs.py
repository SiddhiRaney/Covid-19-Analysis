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

import plotly.express as px

# ---------------- Positivity Proxy (New Cases / Active) ----------------
df_US["PositivityProxy"] = df_US["New cases"] / df_US["Active"]

fig16 = px.line(
    df_US,
    x="Date",
    y="PositivityProxy",
    height=400,
    title="New Cases to Active Cases Ratio (Positivity Proxy)"
)
fig16.show()

# ---------------- Recovered vs Deaths Ratio ----------------
df_US["RecoveredToDeaths"] = df_US["Recovered"] / df_US["Deaths"]

fig17 = px.line(
    df_US,
    x="Date",
    y="RecoveredToDeaths",
    height=400,
    title="Recovered to Deaths Ratio Over Time in the US"
)
fig17.show()

# ---------------- Active Cases Change Per Day ----------------
df_US["ActiveChange"] = df_US["Active"].diff()

fig18 = px.line(
    df_US,
    x="Date",
    y="ActiveChange",
    height=400,
    title="Daily Change in Active COVID-19 Cases in the US"
)
fig18.show()

# ---------------- Deaths per New Case ----------------
df_US["DeathsPerNewCase"] = df_US["New deaths"] / df_US["New cases"]

fig19 = px.line(
    df_US,
    x="Date",
    y="DeathsPerNewCase",
    height=400,
    title="Deaths per New COVID-19 Case in the US"
)
fig19.show()

# ---------------- 14-Day Rolling Avg of New Deaths ----------------
df_US["NewDeaths_14DayAvg"] = df_US["New deaths"].rolling(window=14).mean()

fig20 = px.line(
    df_US,
    x="Date",
    y="NewDeaths_14DayAvg",
    height=400,
    title="14-Day Rolling Average of New Deaths in the US"
)
fig20.show()

# ---------------- Confirmed vs Recovered vs Deaths ----------------
fig21 = px.line(
    df_US,
    x="Date",
    y=["Confirmed", "Recovered", "Deaths"],
    height=400,
    title="Confirmed vs Recovered vs Deaths Over Time in the US"
)
fig21.show()

# ---------------- Recovery Momentum (Daily Recovered Change) ----------------
df_US["RecoveredChange"] = df_US["Recovered"].diff()

fig22 = px.line(
    df_US,
    x="Date",
    y="RecoveredChange",
    height=400,
    title="Daily Change in Recovered Cases in the US"
)
fig22.show()

# ---------------- Log Scale Confirmed Cases ----------------
fig23 = px.line(
    df_US,
    x="Date",
    y="Confirmed",
    height=400,
    title="Log Scale of Confirmed COVID-19 Cases in the US",
    log_y=True
)
fig23.show()
import plotly.express as px
import numpy as np

# ---------------- 7-Day Avg: New Cases vs New Deaths ----------------
df_US["NewCases_7DayAvg"] = df_US["New cases"].rolling(7).mean()
df_US["NewDeaths_7DayAvg"] = df_US["New deaths"].rolling(7).mean()

px.line(df_US, x="Date",
        y=["NewCases_7DayAvg", "NewDeaths_7DayAvg"],
        height=400,
        title="7-Day Avg: New Cases vs New Deaths in the US").show()

# ---------------- Doubling Time ----------------
df_US["DoublingTime"] = 70 / df_US["DailyGrowthRate"]

px.line(df_US, x="Date",
        y="DoublingTime",
        height=400,
        title="COVID-19 Case Doubling Time (Days)").show()

# ---------------- Recovered vs Death % ----------------
df_US["RecoveredPercent"] = df_US["Recovered"] / df_US["Confirmed"] * 100
df_US["DeathsPercent"] = df_US["Deaths"] / df_US["Confirmed"] * 100

px.line(df_US, x="Date",
        y=["RecoveredPercent", "DeathsPercent"],
        height=400,
        title="Recovered vs Deaths (% of Confirmed)").show()

# ---------------- Net Outcome ----------------
df_US["NetOutcome"] = df_US["Recovered"] - df_US["Deaths"]

px.line(df_US, x="Date",
        y="NetOutcome",
        height=400,
        title="Net Outcome (Recovered - Deaths)").show()

# ---------------- Volatility in New Cases ----------------
df_US["CaseVolatility"] = df_US["New cases"].rolling(7).std()

px.line(df_US, x="Date",
        y="CaseVolatility",
        height=400,
        title="7-Day Volatility of New Cases").show()

# ---------------- Death Rate Momentum ----------------
df_US["DeathRateChange"] = df_US["Death Rate"].diff()

px.line(df_US, x="Date",
        y="DeathRateChange",
        height=400,
        title="Change in Death Rate Over Time").show()

# ---------------- Case Surge Detection (Z-Score) ----------------
df_US["CaseZScore"] = (
    (df_US["New cases"] - df_US["New cases"].mean()) /
    df_US["New cases"].std()
)

px.line(df_US, x="Date",
        y="CaseZScore",
        height=400,
        title="COVID-19 Case Surge Detection (Z-Score)").show()

# ---------------- Active vs Closed Cases ----------------
df_US["ClosedCases"] = df_US["Recovered"] + df_US["Deaths"]

px.line(df_US, x="Date",
        y=["Active", "ClosedCases"],
        height=400,
        title="Active vs Closed COVID-19 Cases").show()

# ---------------- Pandemic Control Index ----------------
df_US["ControlIndex"] = df_US["Recovered"] / df_US["Active"]

px.line(df_US, x="Date",
        y="ControlIndex",
        height=400,
        title="Pandemic Control Index (Recovered / Active)").show()

