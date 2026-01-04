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
