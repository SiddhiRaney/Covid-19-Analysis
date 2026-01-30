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

# ---------------- Hospitalization Proxy (Active / Confirmed) ----------------
df_US["HospitalLoadProxy"] = df_US["Active"] / df_US["Confirmed"]

px.line(
    df_US,
    x="Date",
    y="HospitalLoadProxy",
    height=400,
    title="Hospital Load Proxy (Active / Confirmed)"
).show()


# ---------------- Peak Detection: New Cases ----------------
df_US["NewCases_Peak"] = df_US["New cases"].rolling(7).max()

px.line(
    df_US,
    x="Date",
    y=["New cases", "NewCases_Peak"],
    height=400,
    title="New Cases vs Rolling Peak (7-Day)"
).show()


# ---------------- Mortality Momentum (Deaths per Active Case) ----------------
df_US["MortalityMomentum"] = df_US["Deaths"] / df_US["Active"]

px.line(
    df_US,
    x="Date",
    y="MortalityMomentum",
    height=400,
    title="Mortality Momentum (Deaths / Active Cases)"
).show()


# ---------------- Recovery Velocity ----------------
df_US["RecoveryVelocity"] = df_US["Recovered"].pct_change() * 100

px.line(
    df_US,
    x="Date",
    y="RecoveryVelocity",
    height=400,
    title="Recovery Velocity (% Change in Recoveries)"
).show()


# ---------------- Case Load Pressure ----------------
df_US["CaseLoadPressure"] = df_US["New cases"] / df_US["ClosedCases"]

px.line(
    df_US,
    x="Date",
    y="CaseLoadPressure",
    height=400,
    title="Case Load Pressure (New / Closed Cases)"
).show()


# ---------------- Severity Index ----------------
df_US["SeverityIndex"] = df_US["Deaths"] / df_US["Recovered"]

px.line(
    df_US,
    x="Date",
    y="SeverityIndex",
    height=400,
    title="COVID-19 Severity Index (Deaths / Recovered)"
).show()


# ---------------- Stability Index ----------------
df_US["StabilityIndex"] = df_US["Recovered"] / (df_US["New cases"] + 1)

px.line(
    df_US,
    x="Date",
    y="StabilityIndex",
    height=400,
    title="Pandemic Stability Index"
).show()


# ---------------- Transmission Acceleration ----------------
df_US["TransmissionAccel"] = df_US["New cases"].diff().diff()

px.line(
    df_US,
    x="Date",
    y="TransmissionAccel",
    height=400,
    title="Transmission Acceleration (2nd Derivative of New Cases)"
).show()


# ---------------- Death Lag Analysis ----------------
df_US["Deaths_Lag7"] = df_US["New deaths"].shift(-7)

px.line(
    df_US,
    x="Date",
    y=["New cases", "Deaths_Lag7"],
    height=400,
    title="Lag Relationship: New Cases vs Deaths (7-Day Lag)"
).show()


# ---------------- Pandemic Phase Indicator ----------------
df_US["PhaseIndicator"] = (
    (df_US["Recovered"] - df_US["Active"]) / df_US["Confirmed"]
)

px.line(
    df_US,
    x="Date",
    y="PhaseIndicator",
    height=400,
    title="Pandemic Phase Indicator"
).show()
# ---------------- Wave Strength Index ----------------
df_US["WaveStrength"] = df_US["New cases"].rolling(14).max() / (df_US["New cases"].rolling(14).mean() + 1)

px.line(
    df_US,
    x="Date",
    y="WaveStrength",
    height=400,
    title="Wave Strength Index (Peak / Avg New Cases)"
).show()


# ---------------- Recovery Efficiency ----------------
df_US["RecoveryEfficiency"] = df_US["RecoveredChange"] / (df_US["New cases"] + 1)

px.line(
    df_US,
    x="Date",
    y="RecoveryEfficiency",
    height=400,
    title="Recovery Efficiency (Recovered Change / New Cases)"
).show()


# ---------------- Fatality Acceleration ----------------
df_US["FatalityAccel"] = df_US["New deaths"].diff().diff()

px.line(
    df_US,
    x="Date",
    y="FatalityAccel",
    height=400,
    title="Fatality Acceleration (2nd Derivative of Deaths)"
).show()


# ---------------- Case Resolution Speed ----------------
df_US["ResolutionSpeed"] = df_US["ClosedCases"].pct_change() * 100

px.line(
    df_US,
    x="Date",
    y="ResolutionSpeed",
    height=400,
    title="Case Resolution Speed (% Change in Closed Cases)"
).show()


# ---------------- Stress Index ----------------
df_US["StressIndex"] = df_US["Active"] / (df_US["Recovered"] + 1)

px.line(
    df_US,
    x="Date",
    y="StressIndex",
    height=400,
    title="Healthcare Stress Index (Active / Recovered)"
).show()


# ---------------- Infection Momentum ----------------
df_US["InfectionMomentum"] = df_US["New cases"] / df_US["Confirmed"]

px.line(
    df_US,
    x="Date",
    y="InfectionMomentum",
    height=400,
    title="Infection Momentum (New / Confirmed)"
).show()


# ---------------- Death Burden Index ----------------
df_US["DeathBurden"] = df_US["Deaths"] / df_US["Active"]

px.line(
    df_US,
    x="Date",
    y="DeathBurden",
    height=400,
    title="Death Burden Index (Deaths / Active)"
).show()


# ---------------- Recovery Dominance ----------------
df_US["RecoveryDominance"] = df_US["Recovered"] / (df_US["Recovered"] + df_US["Deaths"])

px.line(
    df_US,
    x="Date",
    y="RecoveryDominance",
    height=400,
    title="Recovery Dominance Ratio"
).show()


# ---------------- Pandemic Energy ----------------
df_US["PandemicEnergy"] = df_US["New cases"] * df_US["DailyGrowthRate"]

px.line(
    df_US,
    x="Date",
    y="PandemicEnergy",
    height=400,
    title="Pandemic Energy (New Cases × Growth Rate)"
).show()


# ---------------- Case Exhaustion Index ----------------
df_US["ExhaustionIndex"] = df_US["New cases"].rolling(7).mean() / (df_US["Active"] + 1)

px.line(
    df_US,
    x="Date",
    y="ExhaustionIndex",
    height=400,
    title="Case Exhaustion Index"
).show()


# ---------------- Recovery Lead Indicator ----------------
df_US["RecoveryLead"] = df_US["Recovered"].shift(-7) - df_US["New cases"]

px.line(
    df_US,
    x="Date",
    y="RecoveryLead",
    height=400,
    title="Recovery Lead Indicator (7-Day Lead)"
).show()


# ---------------- Pandemic Pressure Index ----------------
df_US["PressureIndex"] = (
    df_US["New cases"] + df_US["Active"]
) / (df_US["Recovered"] + 1)

px.line(
    df_US,
    x="Date",
    y="PressureIndex",
    height=400,
    title="Pandemic Pressure Index"
).show()


# ---------------- Mortality Risk Trend ----------------
df_US["MortalityRisk"] = df_US["New deaths"] / (df_US["Active"] + 1)

px.line(
    df_US,
    x="Date",
    y="MortalityRisk",
    height=400,
    title="Mortality Risk Trend"
).show()


# ---------------- Recovery Stability ----------------
df_US["RecoveryStability"] = df_US["Recovered"].rolling(14).std()

px.line(
    df_US,
    x="Date",
    y="RecoveryStability",
    height=400,
    title="Recovery Stability (14-Day Std Dev)"
).show()


# ---------------- Pandemic Turning Point Signal ----------------
df_US["TurningPointSignal"] = (
    df_US["New cases"].diff() + df_US["Active"].diff()
)

px.line(
    df_US,
    x="Date",
    y="TurningPointSignal",
    height=400,
    title="Pandemic Turning Point Signal"
).show()
