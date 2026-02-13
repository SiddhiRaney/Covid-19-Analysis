import plotly.express as px

# ---------------- Graph 1: Top 15 countries by Total Cases ----------------
fig1 = px.bar(dataset1.head(15), 
              x='Country/Region', 
              y='TotalCases', 
              color='TotalCases', 
              height=500, 
              hover_data=['Country/Region', 'Continent'])
fig1.show()

# ---------------- Graph 2: Top 15 countries (Total Cases vs Total Deaths) ----------------
fig2 = px.bar(dataset1.head(15), 
              x='Country/Region', 
              y='TotalCases', 
              color='TotalDeaths', 
              height=500, 
              hover_data=['Country/Region', 'Continent'])
fig2.show()

# ---------------- Graph 3: Top 15 countries (Total Cases vs Total Recovered) ----------------
fig3 = px.bar(dataset1.head(15), 
              x='Country/Region', 
              y='TotalCases', 
              color='TotalRecovered', 
              height=500, 
              hover_data=['Country/Region', 'Continent'])
fig3.show()

# ---------------- Graph 4: Top 15 countries (Total Cases vs Total Tests) ----------------
fig4 = px.bar(dataset1.head(15), 
              x='Country/Region', 
              y='TotalCases', 
              color='TotalTests', 
              height=500, 
              hover_data=['Country/Region', 'Continent'])
fig4.show()

# ---------------- Graph 5: Horizontal Bar - Total Tests vs Country ----------------
fig5 = px.bar(dataset1.head(15), 
              x='TotalTests', 
              y='Country/Region', 
              color='TotalTests', 
              orientation='h', 
              height=500, 
              hover_data=['Country/Region', 'Continent'])
fig5.show()

# ---------------- Graph 6: Horizontal Bar - Total Tests vs Continent ----------------
fig6 = px.bar(dataset1.head(15), 
              x='TotalTests', 
              y='Continent', 
              color='TotalTests', 
              orientation='h', 
              height=500, 
              hover_data=['Country/Region', 'Continent'])
fig6.show()
top15 = dataset1.sort_values(by='TotalCases', ascending=False).head(15)

fig1 = px.bar(
    top15,
    x='Country/Region',
    y='TotalCases',
    color='TotalCases',
    height=500,
    hover_data=['Country/Region', 'Continent'],
    title="Top 15 Countries by Total COVID-19 Cases",
    color_continuous_scale='Reds'
)
fig1.show()
# ---------------- Graph 7: Top 15 Countries by Total Deaths ----------------
fig7 = px.bar(
    top15,
    x='Country/Region',
    y='TotalDeaths',
    color='TotalDeaths',
    height=500,
    hover_data=['Country/Region', 'Continent'],
    title="Top 15 Countries by Total COVID-19 Deaths",
    color_continuous_scale='Oranges'
)
fig7.show()


# ---------------- Graph 8: Top 15 Countries by Total Recovered ----------------
fig8 = px.bar(
    top15,
    x='Country/Region',
    y='TotalRecovered',
    color='TotalRecovered',
    height=500,
    hover_data=['Country/Region', 'Continent'],
    title="Top 15 Countries by Total Recoveries",
    color_continuous_scale='Greens'
)
fig8.show()


# ---------------- Graph 9: Scatter Plot - Total Cases vs Deaths ----------------
fig9 = px.scatter(
    top15,
    x='TotalCases',
    y='TotalDeaths',
    size='TotalCases',
    color='Continent',
    hover_name='Country/Region',
    title="Total Cases vs Total Deaths (Top 15 Countries)"
)
fig9.show()


# ---------------- Graph 10: Scatter Plot - Total Cases vs Total Tests ----------------
fig10 = px.scatter(
    top15,
    x='TotalCases',
    y='TotalTests',
    size='TotalTests',
    color='Continent',
    hover_name='Country/Region',
    title="Total Cases vs Total Tests (Top 15 Countries)"
)
fig10.show()


# ---------------- Graph 11: Pie Chart - Share of Total Cases by Continent ----------------
continent_cases = top15.groupby('Continent')['TotalCases'].sum().reset_index()

fig11 = px.pie(
    continent_cases,
    names='Continent',
    values='TotalCases',
    title="Continent-wise Share of Total COVID-19 Cases (Top 15 Countries)"
)
fig11.show()


# ---------------- Graph 12: Bubble Chart - Cases, Deaths & Tests ----------------
fig12 = px.scatter(
    top15,
    x='TotalCases',
    y='TotalDeaths',
    size='TotalTests',
    color='Country/Region',
    hover_name='Country/Region',
    title="Cases vs Deaths with Bubble Size = Total Tests"
)
fig12.show()
# ---------------- Graph 13: Death Rate (%) by Country ----------------
top15['DeathRate'] = (top15['TotalDeaths'] / top15['TotalCases']) * 100

fig13 = px.bar(
    top15,
    x='Country/Region',
    y='DeathRate',
    color='DeathRate',
    height=500,
    hover_data=['Continent'],
    title="COVID-19 Death Rate (%) by Country (Top 15)",
    color_continuous_scale='Reds'
)
fig13.show()


# ---------------- Graph 14: Recovery Rate (%) by Country ----------------
top15['RecoveryRate'] = (top15['TotalRecovered'] / top15['TotalCases']) * 100

fig14 = px.bar(
    top15,
    x='Country/Region',
    y='RecoveryRate',
    color='RecoveryRate',
    height=500,
    hover_data=['Continent'],
    title="COVID-19 Recovery Rate (%) by Country (Top 15)",
    color_continuous_scale='Greens'
)
fig14.show()


# ---------------- Graph 15: Scatter - Total Tests vs Total Deaths ----------------
fig15 = px.scatter(
    top15,
    x='TotalTests',
    y='TotalDeaths',
    size='TotalDeaths',
    color='Continent',
    hover_name='Country/Region',
    title="Total Tests vs Total Deaths (Top 15 Countries)"
)
fig15.show()


# ---------------- Graph 16: Box Plot - Total Cases by Continent ----------------
fig16 = px.box(
    top15,
    x='Continent',
    y='TotalCases',
    color='Continent',
    title="Distribution of Total COVID-19 Cases by Continent"
)
fig16.show()


# ---------------- Graph 17: Correlation Heatmap ----------------
corr = top15[['TotalCases', 'TotalDeaths', 'TotalRecovered', 'TotalTests']].corr()

fig17 = px.imshow(
    corr,
    text_auto=True,
    title="Correlation Heatmap of COVID-19 Metrics"
)
fig17.show()


# ---------------- Graph 18: Stacked Bar - Cases, Deaths & Recovered ----------------
fig18 = px.bar(
    top15,
    x='Country/Region',
    y=['TotalCases', 'TotalDeaths', 'TotalRecovered'],
    title="Cases, Deaths & Recoveries Comparison (Top 15)",
    height=500
)
fig18.show()


# ---------------- Graph 19: Treemap - Cases by Country & Continent ----------------
fig19 = px.treemap(
    top15,
    path=['Continent', 'Country/Region'],
    values='TotalCases',
    title="Treemap of Total COVID-19 Cases by Country and Continent"
)
fig19.show()


# ---------------- Graph 20: Bubble Chart - Recovery Rate vs Death Rate ----------------
fig20 = px.scatter(
    top15,
    x='RecoveryRate',
    y='DeathRate',
    size='TotalCases',
    color='Country/Region',
    hover_name='Country/Region',
    title="Recovery Rate vs Death Rate (Bubble Size = Total Cases)"
)
fig20.show()
# ---------------- Graph 21: Line Chart - Total Cases by Country ----------------
fig21 = px.line(
    top15,
    x='Country/Region',
    y='TotalCases',
    markers=True,
    title="Line Trend of Total COVID-19 Cases (Top 15 Countries)"
)
fig21.show()


# ---------------- Graph 22: Line Chart - Deaths vs Recoveries ----------------
fig22 = px.line(
    top15,
    x='Country/Region',
    y=['TotalDeaths', 'TotalRecovered'],
    title="Deaths vs Recoveries Comparison (Top 15 Countries)"
)
fig22.show()


# ---------------- Graph 23: Sunburst Chart - Continent → Country → Cases ----------------
fig23 = px.sunburst(
    top15,
    path=['Continent', 'Country/Region'],
    values='TotalCases',
    title="Sunburst View of COVID-19 Cases"
)
fig23.show()


# ---------------- Graph 24: Histogram - Distribution of Total Cases ----------------
fig24 = px.histogram(
    top15,
    x='TotalCases',
    nbins=10,
    title="Distribution of Total COVID-19 Cases (Top 15)"
)
fig24.show()


# ---------------- Graph 25: Histogram - Distribution of Death Rate ----------------
fig25 = px.histogram(
    top15,
    x='DeathRate',
    nbins=10,
    title="Distribution of COVID-19 Death Rate (%)"
)
fig25.show()


# ---------------- Graph 26: Violin Plot - Death Rate by Continent ----------------
fig26 = px.violin(
    top15,
    x='Continent',
    y='DeathRate',
    box=True,
    points='all',
    title="Death Rate Distribution by Continent"
)
fig26.show()


# ---------------- Graph 27: Violin Plot - Recovery Rate by Continent ----------------
fig27 = px.violin(
    top15,
    x='Continent',
    y='RecoveryRate',
    box=True,
    points='all',
    title="Recovery Rate Distribution by Continent"
)
fig27.show()


# ---------------- Graph 28: Scatter Matrix (Pair Plot) ----------------
fig28 = px.scatter_matrix(
    top15,
    dimensions=['TotalCases', 'TotalDeaths', 'TotalRecovered', 'TotalTests'],
    color='Continent',
    title="Scatter Matrix of COVID-19 Metrics"
)
fig28.show()


# ---------------- Graph 29: Radar Chart - Country-wise Metrics ----------------
fig29 = px.line_polar(
    top15,
    r='TotalCases',
    theta='Country/Region',
    line_close=True,
    title="Radar Chart of Total Cases (Top 15 Countries)"
)
fig29.show()


# ---------------- Graph 30: Bar Chart - Tests per Case Ratio ----------------
top15['TestsPerCase'] = top15['TotalTests'] / top15['TotalCases']

fig30 = px.bar(
    top15,
    x='Country/Region',
    y='TestsPerCase',
    color='TestsPerCase',
    title="COVID-19 Tests per Case Ratio (Top 15 Countries)"
)
fig30.show()
# ---------------- Graph 31: Active Cases by Country ----------------
top15['ActiveCases'] = top15['TotalCases'] - (top15['TotalDeaths'] + top15['TotalRecovered'])

fig31 = px.bar(
    top15,
    x='Country/Region',
    y='ActiveCases',
    color='ActiveCases',
    title="Active COVID-19 Cases by Country (Top 15)",
    height=500,
    color_continuous_scale='Blues'
)
fig31.show()


# ---------------- Graph 32: Active vs Recovered Cases ----------------
fig32 = px.scatter(
    top15,
    x='ActiveCases',
    y='TotalRecovered',
    size='TotalCases',
    color='Continent',
    hover_name='Country/Region',
    title="Active Cases vs Recovered Cases"
)
fig32.show()


# ---------------- Graph 33: Deaths per Million vs Tests per Million ----------------
top15['DeathsPerMillion'] = (top15['TotalDeaths'] / top15['Population']) * 1e6
top15['TestsPerMillion'] = (top15['TotalTests'] / top15['Population']) * 1e6

fig33 = px.scatter(
    top15,
    x='TestsPerMillion',
    y='DeathsPerMillion',
    size='TotalCases',
    color='Country/Region',
    title="Deaths per Million vs Tests per Million"
)
fig33.show()


# ---------------- Graph 34: Recovery vs Death Rate Comparison ----------------
fig34 = px.bar(
    top15,
    x='Country/Region',
    y=['RecoveryRate', 'DeathRate'],
    title="Recovery Rate vs Death Rate Comparison",
    height=500
)
fig34.show()


# ---------------- Graph 35: Bubble Chart - Active Cases Focus ----------------
fig35 = px.scatter(
    top15,
    x='TotalCases',
    y='ActiveCases',
    size='ActiveCases',
    color='Continent',
    hover_name='Country/Region',
    title="Total Cases vs Active Cases (Bubble = Active Cases)"
)
fig35.show()


# ---------------- Graph 36: Population vs Total Cases ----------------
fig36 = px.scatter(
    top15,
    x='Population',
    y='TotalCases',
    size='TotalCases',
    color='Continent',
    hover_name='Country/Region',
    title="Population vs Total COVID-19 Cases"
)
fig36.show()


# ---------------- Graph 37: Stacked Bar - Active, Recovered, Deaths ----------------
fig37 = px.bar(
    top15,
    x='Country/Region',
    y=['ActiveCases', 'TotalRecovered', 'TotalDeaths'],
    title="Active vs Recovered vs Deaths (Top 15 Countries)",
    height=500
)
fig37.show()


# ---------------- Graph 38: Choropleth Map - Total Cases ----------------
fig38 = px.choropleth(
    top15,
    locations='Country/Region',
    locationmode='country names',
    color='TotalCases',
    hover_name='Country/Region',
    title="World Map of Total COVID-19 Cases (Top 15)",
    color_continuous_scale='Reds'
)
fig38.show()


# ---------------- Graph 39: Choropleth Map - Death Rate ----------------
fig39 = px.choropleth(
    top15,
    locations='Country/Region',
    locationmode='country names',
    color='DeathRate',
    hover_name='Country/Region',
    title="World Map of COVID-19 Death Rate (%)",
    color_continuous_scale='OrRd'
)
fig39.show()


# ---------------- Graph 40: Parallel Coordinates Plot ----------------
fig40 = px.parallel_coordinates(
    top15,
    dimensions=['TotalCases', 'TotalDeaths', 'TotalRecovered', 'TotalTests', 'DeathRate', 'RecoveryRate'],
    color='TotalCases',
    title="Parallel Coordinates Plot of COVID-19 Metrics"
)
fig40.show()
# ---------------- Graph 41: Case Fatality Ratio vs Tests per Case ----------------
fig41 = px.scatter(
    top15,
    x='TestsPerCase',
    y='DeathRate',
    size='TotalCases',
    color='Continent',
    hover_name='Country/Region',
    title="Case Fatality Ratio vs Tests per Case"
)
fig41.show()


# ---------------- Graph 42: Recovery Efficiency Index ----------------
top15['RecoveryEfficiency'] = top15['TotalRecovered'] / top15['ActiveCases']

fig42 = px.bar(
    top15,
    x='Country/Region',
    y='RecoveryEfficiency',
    color='RecoveryEfficiency',
    title="Recovery Efficiency Index by Country",
    height=500,
    color_continuous_scale='Greens'
)
fig42.show()


# ---------------- Graph 43: Mortality Burden Index ----------------
top15['MortalityBurden'] = top15['TotalDeaths'] / top15['Population'] * 1e6

fig43 = px.bar(
    top15,
    x='Country/Region',
    y='MortalityBurden',
    color='MortalityBurden',
    title="Mortality Burden per Million Population",
    height=500,
    color_continuous_scale='Reds'
)
fig43.show()


# ---------------- Graph 44: Active Cases Percentage ----------------
top15['ActiveRate'] = (top15['ActiveCases'] / top15['TotalCases']) * 100

fig44 = px.bar(
    top15,
    x='Country/Region',
    y='ActiveRate',
    color='ActiveRate',
    title="Active Cases Percentage by Country",
    height=500,
    color_continuous_scale='Blues'
)
fig44.show()


# ---------------- Graph 45: Donut Chart - Active vs Closed Cases ----------------
closed_cases = top15[['Country/Region', 'TotalRecovered', 'TotalDeaths']]
closed_cases['ClosedCases'] = closed_cases['TotalRecovered'] + closed_cases['TotalDeaths']

fig45 = px.pie(
    closed_cases,
    names='Country/Region',
    values='ClosedCases',
    hole=0.4,
    title="Closed Cases Distribution (Recovered + Deaths)"
)
fig45.show()


# ---------------- Graph 46: Scatter - Population Density Effect (Proxy) ----------------
fig46 = px.scatter(
    top15,
    x='Population',
    y='ActiveCases',
    size='TotalCases',
    color='Country/Region',
    title="Population vs Active Cases (Density Effect Proxy)"
)
fig46.show()


# ---------------- Graph 47: Normalized Metrics Heatmap ----------------
norm_cols = ['TotalCases', 'TotalDeaths', 'TotalRecovered', 'TotalTests']
norm_data = (top15[norm_cols] - top15[norm_cols].min()) / (top15[norm_cols].max() - top15[norm_cols].min())

fig47 = px.imshow(
    norm_data,
    text_auto=True,
    title="Normalized Heatmap of COVID-19 Metrics"
)
fig47.show()


# ---------------- Graph 48: Rank Comparison - Cases vs Deaths ----------------
top15['CasesRank'] = top15['TotalCases'].rank(ascending=False)
top15['DeathsRank'] = top15['TotalDeaths'].rank(ascending=False)

fig48 = px.scatter(
    top15,
    x='CasesRank',
    y='DeathsRank',
    text='Country/Region',
    title="Rank Comparison: Total Cases vs Total Deaths"
)
fig48.show()


# ---------------- Graph 49: Area Chart - Cumulative Metrics ----------------
fig49 = px.area(
    top15,
    x='Country/Region',
    y=['TotalCases', 'TotalRecovered', 'TotalDeaths'],
    title="Cumulative Area Chart of COVID-19 Metrics"
)
fig49.show()


# ---------------- Graph 50: Funnel Chart - Case Progression ----------------
funnel_data = top15[['Country/Region', 'TotalCases', 'TotalRecovered', 'TotalDeaths']]

fig50 = px.funnel(
    funnel_data,
    x=['TotalCases', 'TotalRecovered', 'TotalDeaths'],
    y='Country/Region',
    title="COVID-19 Case Progression Funnel"
)
fig50.show()
# ---------------- Graph 51: Case Severity Index ----------------
top15['CaseSeverityIndex'] = (top15['TotalDeaths'] / top15['TotalRecovered']) * 100

fig51 = px.bar(
    top15,
    x='Country/Region',
    y='CaseSeverityIndex',
    color='CaseSeverityIndex',
    title="Case Severity Index by Country",
    color_continuous_scale='Reds'
)
fig51.show()


# ---------------- Graph 52: Healthcare Stress Indicator ----------------
top15['HealthcareStress'] = top15['ActiveCases'] / top15['TotalTests']

fig52 = px.scatter(
    top15,
    x='HealthcareStress',
    y='ActiveCases',
    size='TotalCases',
    color='Continent',
    hover_name='Country/Region',
    title="Healthcare Stress vs Active Cases"
)
fig52.show()


# ---------------- Graph 53: Deaths as % of Closed Cases ----------------
top15['DeathShareClosed'] = (top15['TotalDeaths'] / (top15['TotalDeaths'] + top15['TotalRecovered'])) * 100

fig53 = px.bar(
    top15,
    x='Country/Region',
    y='DeathShareClosed',
    color='DeathShareClosed',
    title="Deaths as Percentage of Closed Cases",
    color_continuous_scale='OrRd'
)
fig53.show()


# ---------------- Graph 54: Recovery Momentum ----------------
top15['RecoveryMomentum'] = top15['TotalRecovered'] / top15['TotalCases']

fig54 = px.scatter(
    top15,
    x='RecoveryMomentum',
    y='TotalRecovered',
    size='TotalCases',
    color='Country/Region',
    title="Recovery Momentum Analysis"
)
fig54.show()


# ---------------- Graph 55: Active Case Burden per Million ----------------
top15['ActivePerMillion'] = (top15['ActiveCases'] / top15['Population']) * 1e6

fig55 = px.bar(
    top15,
    x='Country/Region',
    y='ActivePerMillion',
    color='ActivePerMillion',
    title="Active COVID-19 Cases per Million Population",
    color_continuous_scale='Blues'
)
fig55.show()


# ---------------- Graph 56: Testing Effectiveness ----------------
top15['TestingEffectiveness'] = top15['TotalRecovered'] / top15['TotalTests']

fig56 = px.scatter(
    top15,
    x='TotalTests',
    y='TestingEffectiveness',
    size='TotalCases',
    color='Continent',
    title="Testing Effectiveness vs Total Tests"
)
fig56.show()


# ---------------- Graph 57: Deaths vs Active Rate ----------------
fig57 = px.scatter(
    top15,
    x='ActiveRate',
    y='DeathRate',
    size='TotalCases',
    color='Country/Region',
    title="Active Rate vs Death Rate"
)
fig57.show()


# ---------------- Graph 58: Country-wise Metric Profile (Radar - Multi) ----------------
radar_data = top15.melt(
    id_vars=['Country/Region'],
    value_vars=['TotalCases', 'TotalDeaths', 'TotalRecovered']
)

fig58 = px.line_polar(
    radar_data,
    r='value',
    theta='variable',
    color='Country/Region',
    line_close=True,
    title="Multi-Metric Radar Comparison"
)
fig58.show()


# ---------------- Graph 59: Population Share vs Case Share ----------------
top15['CaseShare'] = top15['TotalCases'] / top15['TotalCases'].sum() * 100
top15['PopulationShare'] = top15['Population'] / top15['Population'].sum() * 100

fig59 = px.scatter(
    top15,
    x='PopulationShare',
    y='CaseShare',
    size='TotalCases',
    color='Country/Region',
    title="Population Share vs COVID-19 Case Share"
)
fig59.show()


# ---------------- Graph 60: Country Risk Index ----------------
top15['RiskIndex'] = (top15['DeathRate'] * top15['ActiveRate']) / 100

fig60 = px.bar(
    top15,
    x='Country/Region',
    y='RiskIndex',
    color='RiskIndex',
    title="Overall COVID-19 Risk Index by Country",
    color_continuous_scale='Reds'
)
fig60.show()
# ---------------- Graph 61: Fatality vs Recovery Tradeoff ----------------
fig61 = px.scatter(
    top15,
    x='RecoveryRate',
    y='DeathRate',
    size='ActiveCases',
    color='Continent',
    hover_name='Country/Region',
    title="Fatality vs Recovery Tradeoff (Bubble = Active Cases)"
)
fig61.show()


# ---------------- Graph 62: Testing Coverage (%) ----------------
top15['TestingCoverage'] = (top15['TotalTests'] / top15['Population']) * 100

fig62 = px.bar(
    top15,
    x='Country/Region',
    y='TestingCoverage',
    color='TestingCoverage',
    title="Testing Coverage Percentage by Country",
    color_continuous_scale='Blues'
)
fig62.show()


# ---------------- Graph 63: Active Case Load vs Population ----------------
fig63 = px.scatter(
    top15,
    x='Population',
    y='ActiveCases',
    size='ActiveCases',
    color='Continent',
    title="Active Case Load vs Population"
)
fig63.show()


# ---------------- Graph 64: Recovery Speed Index ----------------
top15['RecoverySpeed'] = top15['TotalRecovered'] / (top15['TotalRecovered'] + top15['ActiveCases'])

fig64 = px.bar(
    top15,
    x='Country/Region',
    y='RecoverySpeed',
    color='RecoverySpeed',
    title="Recovery Speed Index by Country",
    color_continuous_scale='Greens'
)
fig64.show()


# ---------------- Graph 65: Death Burden vs Case Burden ----------------
fig65 = px.scatter(
    top15,
    x='CaseShare',
    y='DeathShareClosed',
    size='TotalCases',
    color='Country/Region',
    title="Death Burden vs Case Burden"
)
fig65.show()


# ---------------- Graph 66: Tests Needed per Death ----------------
top15['TestsPerDeath'] = top15['TotalTests'] / top15['TotalDeaths']

fig66 = px.bar(
    top15,
    x='Country/Region',
    y='TestsPerDeath',
    color='TestsPerDeath',
    title="Tests Needed per Death",
    color_continuous_scale='Purples'
)
fig66.show()


# ---------------- Graph 67: Active Case Dominance ----------------
fig67 = px.bar(
    top15,
    x='Country/Region',
    y=['ActiveCases', 'TotalRecovered'],
    title="Active vs Recovered Case Dominance",
    height=500
)
fig67.show()


# ---------------- Graph 68: Population Risk Exposure ----------------
top15['PopulationRisk'] = top15['ActiveCases'] / top15['Population'] * 100

fig68 = px.bar(
    top15,
    x='Country/Region',
    y='PopulationRisk',
    color='PopulationRisk',
    title="Population Risk Exposure (%)",
    color_continuous_scale='Reds'
)
fig68.show()


# ---------------- Graph 69: Healthcare Load Index ----------------
top15['HealthcareLoad'] = top15['ActiveCases'] / top15['TotalRecovered']

fig69 = px.scatter(
    top15,
    x='HealthcareLoad',
    y='ActiveCases',
    size='TotalCases',
    color='Continent',
    title="Healthcare Load Index vs Active Cases"
)
fig69.show()


# ---------------- Graph 70: Composite Severity Score ----------------
top15['SeverityScore'] = (
    top15['DeathRate'] * 0.5 +
    top15['ActiveRate'] * 0.3 +
    top15['TestingCoverage'] * 0.2
)

fig70 = px.bar(
    top15,
    x='Country/Region',
    y='SeverityScore',
    color='SeverityScore',
    title="Composite COVID-19 Severity Score",
    color_continuous_scale='OrRd'
)
fig70.show()
# ===================== ADDITIONAL VISUALIZATIONS (71–80) =====================

# ---------------- Graph 71: Cases per Million ----------------
top15['CasesPerMillion'] = (top15['TotalCases'] / top15['Population']) * 1e6

fig71 = px.bar(
    top15,
    x='Country/Region',
    y='CasesPerMillion',
    color='CasesPerMillion',
    title="COVID-19 Cases per Million Population",
    color_continuous_scale='Reds'
)
fig71.show()


# ---------------- Graph 72: Recovery Rate vs Testing Coverage ----------------
fig72 = px.scatter(
    top15,
    x='TestingCoverage',
    y='RecoveryRate',
    size='TotalCases',
    color='Continent',
    title="Recovery Rate vs Testing Coverage"
)
fig72.show()


# ---------------- Graph 73: Mortality vs Population Risk ----------------
fig73 = px.scatter(
    top15,
    x='PopulationRisk',
    y='DeathRate',
    size='TotalCases',
    color='Country/Region',
    title="Mortality vs Population Risk"
)
fig73.show()


# ---------------- Graph 74: Active Case Ratio Heatmap ----------------
heat_data = top15.pivot_table(
    values='ActiveRate',
    index='Continent',
    columns='Country/Region'
)

fig74 = px.imshow(
    heat_data,
    title="Active Case Ratio Heatmap"
)
fig74.show()


# ---------------- Graph 75: Cases vs Recovery Efficiency ----------------
fig75 = px.scatter(
    top15,
    x='TotalCases',
    y='RecoveryEfficiency',
    size='ActiveCases',
    color='Continent',
    title="Total Cases vs Recovery Efficiency"
)
fig75.show()


# ---------------- Graph 76: Testing Coverage Distribution ----------------
fig76 = px.histogram(
    top15,
    x='TestingCoverage',
    nbins=10,
    title="Distribution of Testing Coverage"
)
fig76.show()


# ---------------- Graph 77: Active Burden vs Severity Score ----------------
fig77 = px.scatter(
    top15,
    x='ActivePerMillion',
    y='SeverityScore',
    size='TotalCases',
    color='Country/Region',
    title="Active Burden vs Severity Score"
)
fig77.show()


# ---------------- Graph 78: Tests vs Recovery Momentum ----------------
fig78 = px.scatter(
    top15,
    x='TotalTests',
    y='RecoveryMomentum',
    size='TotalCases',
    color='Continent',
    title="Testing vs Recovery Momentum"
)
fig78.show()


# ---------------- Graph 79: Severity Score Distribution ----------------
fig79 = px.box(
    top15,
    y='SeverityScore',
    title="Severity Score Distribution"
)
fig79.show()


# ---------------- Graph 80: Ranking by Severity Score ----------------
severity_rank = top15.sort_values('SeverityScore', ascending=False)

fig80 = px.bar(
    severity_rank,
    x='Country/Region',
    y='SeverityScore',
    color='SeverityScore',
    title="Country Ranking by Severity Score",
    color_continuous_scale='OrRd'
)
fig80.show()
# ===================== ADDITIONAL VISUALIZATIONS (81–90) =====================

# ---------------- Graph 81: Log Scale Cases vs Deaths ----------------
fig81 = px.scatter(
    top15,
    x='TotalCases',
    y='TotalDeaths',
    log_x=True,
    log_y=True,
    color='Continent',
    title="Log Scale: Total Cases vs Total Deaths"
)
fig81.show()


# ---------------- Graph 82: Cases vs Population (Normalized) ----------------
fig82 = px.scatter(
    top15,
    x='Population',
    y='CasesPerMillion',
    size='TotalCases',
    color='Continent',
    title="Population vs Cases per Million"
)
fig82.show()


# ---------------- Graph 83: Death Rate Trend Line ----------------
fig83 = px.scatter(
    top15,
    x='TotalCases',
    y='DeathRate',
    trendline="ols",
    color='Continent',
    title="Death Rate Trend vs Total Cases"
)
fig83.show()


# ---------------- Graph 84: Recovery vs Active Ratio ----------------
top15['RecoveryActiveRatio'] = top15['TotalRecovered'] / top15['ActiveCases']

fig84 = px.bar(
    top15,
    x='Country/Region',
    y='RecoveryActiveRatio',
    color='RecoveryActiveRatio',
    title="Recovery to Active Case Ratio"
)
fig84.show()


# ---------------- Graph 85: Polar Chart - Death Rate ----------------
fig85 = px.line_polar(
    top15,
    r='DeathRate',
    theta='Country/Region',
    line_close=True,
    title="Polar Plot of Death Rate"
)
fig85.show()


# ---------------- Graph 86: Cases vs Tests Density ----------------
fig86 = px.density_contour(
    top15,
    x='TotalCases',
    y='TotalTests',
    title="Density Contour: Cases vs Tests"
)
fig86.show()


# ---------------- Graph 87: Strip Plot - Death Rate by Continent ----------------
fig87 = px.strip(
    top15,
    x='Continent',
    y='DeathRate',
    color='Continent',
    title="Death Rate Distribution by Continent"
)
fig87.show()


# ---------------- Graph 88: ECDF Plot - Total Cases ----------------
fig88 = px.ecdf(
    top15,
    x='TotalCases',
    color='Continent',
    title="ECDF of Total Cases"
)
fig88.show()


# ---------------- Graph 89: Active vs Death Burden ----------------
fig89 = px.scatter(
    top15,
    x='ActiveCases',
    y='MortalityBurden',
    size='TotalCases',
    color='Country/Region',
    title="Active Cases vs Mortality Burden"
)
fig89.show()


# ---------------- Graph 90: Sorted Line Plot - Recovery Rate ----------------
sorted_rr = top15.sort_values('RecoveryRate')

fig90 = px.line(
    sorted_rr,
    x='Country/Region',
    y='RecoveryRate',
    markers=True,
    title="Sorted Recovery Rate by Country"
)
fig90.show()
