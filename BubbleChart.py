# Step 5 & 6: Data Visualization using Bubble Charts (Continent-wise and Country-wise)

# Importing required library
import plotly.express as px

# --------------------------- STEP 5: CONTINENT-WISE VISUALIZATION ---------------------------

# Scatter plot - Continent vs TotalCases
fig1 = px.scatter(dataset1, 
                  x='Continent', 
                  y='TotalCases',
                  hover_data=['Country/Region', 'Continent'],  # Data shown when hovering
                  color='TotalCases',  # Bubble color based on total cases
                  size='TotalCases',   # Bubble size based on total cases
                  size_max=80)         # Maximum bubble size
fig1.show()

# Scatter plot - Continent vs TotalCases (log_y = True)
# Using log scale on Y-axis to better visualize large differences
fig2 = px.scatter(dataset1.head(57), 
                  x='Continent', 
                  y='TotalCases',
                  hover_data=['Country/Region', 'Continent'], 
                  color='TotalCases', 
                  size='TotalCases', 
                  size_max=80, 
                  log_y=True)
fig2.show()

# Scatter plot - Continent vs TotalTests
# Shows how many total tests were conducted per continent
fig3 = px.scatter(dataset1.head(54), 
                  x='Continent', 
                  y='TotalTests',
                  hover_data=['Country/Region', 'Continent'], 
                  color='TotalTests', 
                  size='TotalTests', 
                  size_max=80)
fig3.show()

# Scatter plot - Continent vs TotalTests (log_y=True)
# Same as above but using logarithmic Y-axis for clearer comparison
fig4 = px.scatter(dataset1.head(50), 
                  x='Continent', 
                  y='TotalTests',
                  hover_data=['Country/Region', 'Continent'], 
                  color='TotalTests', 
                  size='TotalTests', 
                  size_max=80, 
                  log_y=True)
fig4.show()


# --------------------------- STEP 6: COUNTRY-WISE VISUALIZATION ---------------------------

# Bubble chart - Country vs TotalCases (top 100 countries)
# Shows total cases by country to compare spread
fig5 = px.scatter(dataset1.head(100), 
                  x='Country/Region', 
                  y='TotalCases', 
                  hover_data=['Country/Region', 'Continent'], 
                  color='TotalCases', 
                  size='TotalCases', 
                  size_max=80)
fig5.show()

# Bubble chart - Country vs TotalCases (top 30, log_y=True)
# Using log scale for better visual clarity among smaller countries
fig6 = px.scatter(dataset1.head(30), 
                  x='Country/Region', 
                  y='TotalCases', 
                  hover_data=['Country/Region', 'Continent'], 
                  color='Country/Region', 
                  size='TotalCases', 
                  size_max=80, 
                  log_y=True)
fig6.show()

# Bubble chart - Country vs TotalDeaths (top 10 countries)
# Shows total deaths per country (bubble color and size based on deaths)
fig7 = px.scatter(dataset1.head(10), 
                  x='Country/Region', 
                  y='TotalDeaths', 
                  hover_data=['Country/Region', 'Continent'], 
                  color='Country/Region', 
                  size='TotalDeaths', 
                  size_max=80)
fig7.show()

# Bubble chart - Country vs Tests/1M pop (top 30 countries)
# Shows the number of tests per million population
fig8 = px.scatter(dataset1.head(30), 
                  x='Country/Region', 
                  y='Tests/1M pop', 
                  hover_data=['Country/Region', 'Continent'], 
                  color='Country/Region', 
                  size='Tests/1M pop', 
                  size_max=80)
fig8.show()

# Bubble chart - Country vs Tests/1M pop (color scaled by test count)
fig9 = px.scatter(dataset1.head(30), 
                  x='Country/Region', 
                  y='Tests/1M pop', 
                  hover_data=['Country/Region', 'Continent'], 
                  color='Tests/1M pop', 
                  size='Tests/1M pop', 
                  size_max=80)
fig9.show()

# Bubble chart - TotalCases vs TotalDeaths (top 30 countries)
# Visualizing relationship between total cases and total deaths
fig10 = px.scatter(dataset1.head(30), 
                   x='TotalCases', 
                   y='TotalDeaths', 
                   hover_data=['Country/Region', 'Continent'], 
                   color='TotalDeaths', 
                   size='TotalDeaths', 
                   size_max=80)
fig10.show()

# Bubble chart - TotalCases vs TotalDeaths (with log_x and log_y)
# Log scale makes the linear relationship clearer even for smaller values
fig11 = px.scatter(dataset1.head(30), 
                   x='TotalCases', 
                   y='TotalDeaths', 
                   hover_data=['Country/Region', 'Continent'], 
                   color='TotalDeaths', 
                   size='TotalDeaths', 
                   size_max=80, 
                   log_x=True, 
                   log_y=True)
fig11.show()

# Bubble chart - TotalTests vs TotalCases (with log scales)
# Shows correlation between testing volume and total reported cases
fig12 = px.scatter(dataset1.head(30), 
                   x='TotalTests', 
                   y='TotalCases', 
                   hover_data=['Country/Region', 'Continent'], 
                   color='TotalTests', 
                   size='TotalTests', 
                   size_max=80, 
                   log_x=True, 
                   log_y=True)
fig12.show()

# --------------------------- STEP 7: RATE-BASED VISUALIZATIONS ---------------------------

# Bubble chart - Country vs Deaths per 1M population
# Shows mortality impact relative to population size
fig13 = px.scatter(dataset1.head(30),
                   x='Country/Region',
                   y='Deaths/1M pop',
                   hover_data=['Country/Region', 'Continent'],
                   color='Deaths/1M pop',
                   size='Deaths/1M pop',
                   size_max=80)
fig13.show()

# Bubble chart - Country vs Cases per 1M population
# Indicates spread intensity adjusted for population
fig14 = px.scatter(dataset1.head(30),
                   x='Country/Region',
                   y='Cases/1M pop',
                   hover_data=['Country/Region', 'Continent'],
                   color='Cases/1M pop',
                   size='Cases/1M pop',
                   size_max=80)
fig14.show()

# --------------------------- STEP 11: RECOVERY ANALYSIS ---------------------------

# Bubble chart - TotalCases vs TotalRecovered
# Shows recovery trend with respect to total cases
fig22 = px.scatter(dataset1.head(30),
                   x='TotalCases',
                   y='TotalRecovered',
                   hover_data=['Country/Region', 'Continent'],
                   color='TotalRecovered',
                   size='TotalRecovered',
                   size_max=80,
                   log_x=True,
                   log_y=True)
fig22.show()

# Bubble chart - Recovery Rate vs Death Rate
# Compares how well countries recover vs mortality
fig23 = px.scatter(dataset1.head(30),
                   x='RecoveryRate',
                   y='DeathRate',
                   hover_data=['Country/Region', 'Continent'],
                   color='RecoveryRate',
                   size='RecoveryRate',
                   size_max=80)
fig23.show()


# --------------------------- STEP 12: ACTIVE CASES ANALYSIS ---------------------------

# Bubble chart - Country vs ActiveCases
# Highlights ongoing burden on healthcare systems
fig24 = px.scatter(dataset1.head(30),
                   x='Country/Region',
                   y='ActiveCases',
                   hover_data=['Country/Region', 'Continent'],
                   color='ActiveCases',
                   size='ActiveCases',
                   size_max=80)
fig24.show()

# Bubble chart - ActiveCases vs TotalCases
# Shows proportion of unresolved cases
fig25 = px.scatter(dataset1.head(30),
                   x='TotalCases',
                   y='ActiveCases',
                   hover_data=['Country/Region', 'Continent'],
                   color='ActiveCases',
                   size='ActiveCases',
                   size_max=80,
                   log_x=True,
                   log_y=True)
fig25.show()


# --------------------------- STEP 13: SEVERITY ANALYSIS ---------------------------

# Bubble chart - Serious/Critical vs TotalCases
# Indicates strain on critical care infrastructure
fig26 = px.scatter(dataset1.head(30),
                   x='TotalCases',
                   y='Serious/Critical',
                   hover_data=['Country/Region', 'Continent'],
                   color='Serious/Critical',
                   size='Serious/Critical',
                   size_max=80,
                   log_x=True,
                   log_y=True)
fig26.show()

# Bubble chart - Serious/Critical per 1M vs Deaths per 1M
fig27 = px.scatter(dataset1.head(30),
                   x='Serious/Critical/1M pop',
                   y='Deaths/1M pop',
                   hover_data=['Country/Region', 'Continent'],
                   color='Deaths/1M pop',
                   size='Deaths/1M pop',
                   size_max=80)
fig27.show()


# --------------------------- STEP 14: CONTINENT-LEVEL INSIGHT ---------------------------

# Bubble chart - Continent vs TotalCases
fig28 = px.scatter(dataset1,
                   x='Continent',
                   y='TotalCases',
                   hover_data=['Country/Region'],
                   color='Continent',
                   size='TotalCases',
                   size_max=80,
                   log_y=True)
fig28.show()

# Bubble chart - Continent vs TotalDeaths
fig29 = px.scatter(dataset1,
                   x='Continent',
                   y='TotalDeaths',
                   hover_data=['Country/Region'],
                   color='Continent',
                   size='TotalDeaths',
                   size_max=80,
                   log_y=True)
fig29.show()


# --------------------------- STEP 15: TESTING VS OUTCOME ---------------------------

# Bubble chart - Tests per 1M vs Recovery Rate
# Measures effectiveness of testing on recovery
fig30 = px.scatter(dataset1.head(30),
                   x='Tests/1M pop',
                   y='RecoveryRate',
                   hover_data=['Country/Region', 'Continent'],
                   color='RecoveryRate',
                   size='RecoveryRate',
                   size_max=80,
                   log_x=True)
fig30.show()

# Bubble chart - Tests per 1M vs Death Rate
fig31 = px.scatter(dataset1.head(30),
                   x='Tests/1M pop',
                   y='DeathRate',
                   hover_data=['Country/Region', 'Continent'],
                   color='DeathRate',



# --------------------------- STEP 8: CORRELATION ANALYSIS ---------------------------

# Bubble chart - Cases per 1M vs Deaths per 1M
# Helps identify countries with high fatality rates
fig15 = px.scatter(dataset1.head(30),
                   x='Cases/1M pop',
                   y='Deaths/1M pop',
                   hover_data=['Country/Region', 'Continent'],
                   color='Deaths/1M pop',
                   size='Deaths/1M pop',
                   size_max=80)
fig15.show()

# Bubble chart - Tests per 1M vs Cases per 1M (log scale)
# Shows how testing intensity relates to detected cases
fig16 = px.scatter(dataset1.head(30),
                   x='Tests/1M pop',
                   y='Cases/1M pop',
                   hover_data=['Country/Region', 'Continent'],
                   color='Tests/1M pop',
                   size='Tests/1M pop',
                   size_max=80,
                   log_x=True,
                   log_y=True)
fig16.show()


# --------------------------- STEP 9: CONTINENT COMPARISON (AGGREGATED VIEW) ---------------------------

# Bubble chart - Continent vs Average Cases per 1M
fig17 = px.scatter(dataset1,
                   x='Continent',
                   y='Cases/1M pop',
                   hover_data=['Country/Region'],
                   color='Continent',
                   size='Cases/1M pop',
                   size_max=80)
fig17.show()

# Bubble chart - Continent vs Deaths per 1M (log scale)
fig18 = px.scatter(dataset1,
                   x='Continent',
                   y='Deaths/1M pop',
                   hover_data=['Country/Region'],
                   color='Continent',
                   size='Deaths/1M pop',
                   size_max=80,
                   log_y=True)
fig18.show()


# --------------------------- STEP 10: TESTING EFFICIENCY ---------------------------

# Bubble chart - TotalTests vs TotalDeaths
# Evaluates whether higher testing correlates with lower deaths
fig19 = px.scatter(dataset1.head(30),
                   x='TotalTests',
                   y='TotalDeaths',
                   hover_data=['Country/Region', 'Continent'],
                   color='TotalTests',
                   size='TotalTests',
                   size_max=80,
                   log_x=True,
                   log_y=True)
fig19.show()

# Bubble chart - Tests per 1M vs Deaths per 1M
# Shows effectiveness of testing on reducing mortality
fig20 = px.scatter(dataset1.head(30),
                   x='Tests/1M pop',
                   y='Deaths/1M pop',
                   hover_data=['Country/Region', 'Continent'],
                   color='Deaths/1M pop',
                   size='Deaths/1M pop',
                   size_max=80,
                   log_x=True)
fig20.show()

# Bubble chart - TotalCases vs Death Rate (%)
# Shows how deadly the spread is relative to cases
fig21 = px.scatter(dataset1.head(30),
                   x='TotalCases',
                   y='DeathRate',
                   hover_data=['Country/Region', 'Continent'],
                   color='DeathRate',
                   size='DeathRate',
                   size_max=80,
                   log_x=True)
fig21.show()
# --------------------------- STEP 16: POSITIVITY & BURDEN ANALYSIS ---------------------------

# Bubble chart - Positivity Proxy: TotalCases vs TotalTests
# Higher cases with lower tests may indicate under-testing
fig32 = px.scatter(dataset1.head(30),
                   x='TotalTests',
                   y='TotalCases',
                   hover_data=['Country/Region', 'Continent'],
                   color='TotalCases',
                   size='TotalCases',
                   size_max=80,
                   log_x=True,
                   log_y=True)
fig32.show()

# Bubble chart - Cases per Test Ratio
# Indicates how widespread infection is relative to testing
dataset1['Cases_per_Test'] = dataset1['TotalCases'] / dataset1['TotalTests']

fig33 = px.scatter(dataset1.head(30),
                   x='Country/Region',
                   y='Cases_per_Test',
                   hover_data=['Country/Region', 'Continent'],
                   color='Cases_per_Test',
                   size='Cases_per_Test',
                   size_max=80)
fig33.show()


# --------------------------- STEP 17: ACTIVE CASE LOAD ANALYSIS ---------------------------

# Bubble chart - ActiveCases vs Population-adjusted Cases
fig34 = px.scatter(dataset1.head(30),
                   x='Cases/1M pop',
                   y='ActiveCases',
                   hover_data=['Country/Region', 'Continent'],
                   color='ActiveCases',
                   size='ActiveCases',
                   size_max=80,
                   log_y=True)
fig34.show()

# Bubble chart - Active Ratio vs Death Rate
dataset1['ActiveRatio'] = dataset1['ActiveCases'] / dataset1['TotalCases']

fig35 = px.scatter(dataset1.head(30),
                   x='ActiveRatio',
                   y='DeathRate',
                   hover_data=['Country/Region', 'Continent'],
                   color='ActiveRatio',
                   size='ActiveRatio',
                   size_max=80)
fig35.show()


# --------------------------- STEP 18: FATALITY & RECOVERY BALANCE ---------------------------

# Bubble chart - Recovery Rate vs Cases per 1M
fig36 = px.scatter(dataset1.head(30),
                   x='Cases/1M pop',
                   y='RecoveryRate',
                   hover_data=['Country/Region', 'Continent'],
                   color='RecoveryRate',
                   size='RecoveryRate',
                   size_max=80)
fig36.show()

# Bubble chart - Death Rate vs Cases per 1M
fig37 = px.scatter(dataset1.head(30),
                   x='Cases/1M pop',
                   y='DeathRate',
                   hover_data=['Country/Region', 'Continent'],
                   color='DeathRate',
                   size='DeathRate',
                   size_max=80)
fig37.show()


# --------------------------- STEP 19: CONTINENT-WISE AGGREGATED METRICS ---------------------------

# Aggregating continent-level data
continent_df = dataset1.groupby('Continent').mean(numeric_only=True).reset_index()

# Bubble chart - Continent vs Avg Death Rate
fig38 = px.scatter(continent_df,
                   x='Continent',
                   y='DeathRate',
                   color='DeathRate',
                   size='DeathRate',
                   size_max=80)
fig38.show()

# Bubble chart - Continent vs Avg Recovery Rate
fig39 = px.scatter(continent_df,
                   x='Continent',
                   y='RecoveryRate',
                   color='RecoveryRate',
                   size='RecoveryRate',
                   size_max=80)
fig39.show()


# --------------------------- STEP 20: HEALTHCARE STRESS INDICATORS ---------------------------

# Bubble chart - Serious/Critical vs ActiveCases
fig40 = px.scatter(dataset1.head(30),
                   x='ActiveCases',
                   y='Serious/Critical',
                   hover_data=['Country/Region', 'Continent'],
                   color='Serious/Critical',
                   size='Serious/Critical',
                   size_max=80,
                   log_x=True,
                   log_y=True)
fig40.show()

# Bubble chart - Serious/Critical per 1M vs ActiveCases per 1M
dataset1['Active/1M pop'] = dataset1['ActiveCases'] / (dataset1['Population'] / 1_000_000)

fig41 = px.scatter(dataset1.head(30),
                   x='Active/1M pop',
                   y='Serious/Critical/1M pop',
                   hover_data=['Country/Region', 'Continent'],
                   color='Serious/Critical/1M pop',
                   size='Serious/Critical/1M pop',
                   size_max=80)
fig41.show()
# --------------------------- STEP 21: VACCINATION IMPACT ANALYSIS ---------------------------

# Bubble chart - Vaccination Rate vs Cases per 1M
# Shows how vaccination coverage impacts spread
fig42 = px.scatter(dataset1.head(30),
                   x='VaccinationRate',
                   y='Cases/1M pop',
                   hover_data=['Country/Region', 'Continent'],
                   color='VaccinationRate',
                   size='VaccinationRate',
                   size_max=80)
fig42.show()

# Bubble chart - Vaccination Rate vs Death Rate
fig43 = px.scatter(dataset1.head(30),
                   x='VaccinationRate',
                   y='DeathRate',
                   hover_data=['Country/Region', 'Continent'],
                   color='DeathRate',
                   size='DeathRate',
                   size_max=80)
fig43.show()


# --------------------------- STEP 22: POPULATION IMPACT ANALYSIS ---------------------------

# Bubble chart - Population vs TotalCases
fig44 = px.scatter(dataset1.head(30),
                   x='Population',
                   y='TotalCases',
                   hover_data=['Country/Region', 'Continent'],
                   color='TotalCases',
                   size='TotalCases',
                   size_max=80,
                   log_x=True,
                   log_y=True)
fig44.show()

# Bubble chart - Population vs Deaths per 1M
fig45 = px.scatter(dataset1.head(30),
                   x='Population',
                   y='Deaths/1M pop',
                   hover_data=['Country/Region', 'Continent'],
                   color='Deaths/1M pop',
                   size='Deaths/1M pop',
                   size_max=80,
                   log_x=True)
fig45.show()


# --------------------------- STEP 23: TESTING ADEQUACY ANALYSIS ---------------------------

# Bubble chart - Tests per Case
dataset1['Tests_per_Case'] = dataset1['TotalTests'] / dataset1['TotalCases']

fig46 = px.scatter(dataset1.head(30),
                   x='Country/Region',
                   y='Tests_per_Case',
                   hover_data=['Country/Region', 'Continent'],
                   color='Tests_per_Case',
                   size='Tests_per_Case',
                   size_max=80)
fig46.show()

# Bubble chart - Tests per Case vs Death Rate
fig47 = px.scatter(dataset1.head(30),
                   x='Tests_per_Case',
                   y='DeathRate',
                   hover_data=['Country/Region', 'Continent'],
                   color='DeathRate',
                   size='DeathRate',
                   size_max=80)
fig47.show()


# --------------------------- STEP 24: PANDEMIC SEVERITY INDEX ---------------------------

# Creating a composite severity score
dataset1['SeverityIndex'] = (
    dataset1['Deaths/1M pop'] * 0.4 +
    dataset1['Serious/Critical/1M pop'] * 0.3 +
    dataset1['Cases/1M pop'] * 0.3
)

# Bubble chart - Country vs Severity Index
fig48 = px.scatter(dataset1.head(30),
                   x='Country/Region',
                   y='SeverityIndex',
                   hover_data=['Country/Region', 'Continent'],
                   color='SeverityIndex',
                   size='SeverityIndex',
                   size_max=80)
fig48.show()

# Bubble chart - Severity Index vs Recovery Rate
fig49 = px.scatter(dataset1.head(30),
                   x='SeverityIndex',
                   y='RecoveryRate',
                   hover_data=['Country/Region', 'Continent'],
                   color='RecoveryRate',
                   size='RecoveryRate',
                   size_max=80)
fig49.show()


# --------------------------- STEP 25: CONTINENTAL RISK COMPARISON ---------------------------

# Bubble chart - Continent vs Avg Severity Index
continent_severity = dataset1.groupby('Continent')['SeverityIndex'].mean().reset_index()

fig50 = px.scatter(continent_severity,
                   x='Continent',
                   y='SeverityIndex',
                   color='SeverityIndex',
                   size='SeverityIndex',
                   size_max=80)
fig50.show()


# --------------------------- STEP 26: HEALTHCARE CAPACITY STRESS ---------------------------

# Bubble chart - Critical Ratio vs Active Ratio
dataset1['CriticalRatio'] = dataset1['Serious/Critical'] / dataset1['ActiveCases']

fig51 = px.scatter(dataset1.head(30),
                   x='Critical
# --------------------------- STEP 26: HEALTHCARE CAPACITY STRESS (CONTINUED) ---------------------------

# Bubble chart - Critical Ratio vs Active Ratio
dataset1['CriticalRatio'] = dataset1['Serious/Critical'] / dataset1['ActiveCases']

fig51 = px.scatter(dataset1.head(30),
                   x='ActiveRatio',
                   y='CriticalRatio',
                   hover_data=['Country/Region', 'Continent'],
                   color='CriticalRatio',
                   size='CriticalRatio',
                   size_max=80)
fig51.show()


# --------------------------- STEP 27: CASE FATALITY DYNAMICS ---------------------------

# Bubble chart - Case Fatality Rate vs Total Cases
fig52 = px.scatter(dataset1.head(30),
                   x='TotalCases',
                   y='DeathRate',
                   hover_data=['Country/Region', 'Continent'],
                   color='DeathRate',
                   size='DeathRate',
                   size_max=80,
                   log_x=True)
fig52.show()

# Bubble chart - Case Fatality Rate vs Tests per Case
fig53 = px.scatter(dataset1.head(30),
                   x='Tests_per_Case',
                   y='DeathRate',
                   hover_data=['Country/Region', 'Continent'],
                   color='DeathRate',
                   size='DeathRate',
                   size_max=80)
fig53.show()


# --------------------------- STEP 28: TESTING EFFECTIVENESS ---------------------------

# Bubble chart - Tests per 1M vs Tests per Case
fig54 = px.scatter(dataset1.head(30),
                   x='Tests/1M pop',
                   y='Tests_per_Case',
                   hover_data=['Country/Region', 'Continent'],
                   color='Tests_per_Case',
                   size='Tests_per_Case',
                   size_max=80,
                   log_x=True)
fig54.show()

# Bubble chart - Tests per Case vs Recovery Rate
fig55 = px.scatter(dataset1.head(30),
                   x='Tests_per_Case',
                   y='RecoveryRate',
                   hover_data=['Country/Region', 'Continent'],
                   color='RecoveryRate',
                   size='RecoveryRate',
                   size_max=80)
fig55.show()


# --------------------------- STEP 29: ACTIVE BURDEN VS OUTCOME ---------------------------

# Bubble chart - ActiveCases vs Death Rate
fig56 = px.scatter(dataset1.head(30),
                   x='ActiveCases',
                   y='DeathRate',
                   hover_data=['Country/Region', 'Continent'],
                   color='DeathRate',
                   size='DeathRate',
                   size_max=80,
                   log_x=True)
fig56.show()

# Bubble chart - ActiveCases per 1M vs Recovery Rate
fig57 = px.scatter(dataset1.head(30),
                   x='Active/1M pop',
                   y='RecoveryRate',
                   hover_data=['Country/Region', 'Continent'],
                   color='RecoveryRate',
                   size='RecoveryRate',
                   size_max=80)
fig57.show()


# --------------------------- STEP 30: PANDEMIC CONTROL INDICATORS ---------------------------

# Bubble chart - Positivity Proxy vs Death Rate
fig58 = px.scatter(dataset1.head(30),
                   x='Cases_per_Test',
                   y='DeathRate',
                   hover_data=['Country/Region', 'Continent'],
                   color='Cases_per_Test',
                   size='Cases_per_Test',
                   size_max=80)
fig58.show()

# Bubble chart - Positivity Proxy vs Recovery Rate
fig59 = px.scatter(dataset1.head(30),
                   x='Cases_per_Test',
                   y='RecoveryRate',
                   hover_data=['Country/Region', 'Continent'],
                   color='RecoveryRate',
                   size='RecoveryRate',
                   size_max=80)
fig59.show()


# --------------------------- STEP 31: GLOBAL RISK PROFILING ---------------------------

# Bubble chart - Severity Index vs Death Rate
fig60 = px.scatter(dataset1.head(30),
                   x='SeverityIndex',
                   y='DeathRate',
                   hover_data=['Country/Region', 'Continent'],
                   color='SeverityIndex',
                   size='SeverityIndex',
                   size_max=80)
fig60.show()

# Bubble chart - Severity Index vs Active Ratio
fig61 = px.scatter(dataset1.head(30),
                   x='SeverityIndex',
                   y='ActiveRatio',
                   hover_data=['Country/Region', 'Continent'],
                   color='ActiveRatio',
                   size='ActiveRatio',
                   size_max=80)
fig61.show()
# --------------------------- STEP 32: MORTALITY PRESSURE ANALYSIS ---------------------------

# Bubble chart - Deaths vs Serious/Critical
fig62 = px.scatter(dataset1.head(30),
                   x='Serious/Critical',
                   y='TotalDeaths',
                   hover_data=['Country/Region', 'Continent'],
                   color='TotalDeaths',
                   size='Serious/Critical',
                   size_max=80,
                   log_x=True,
                   log_y=True)
fig62.show()


# --------------------------- STEP 33: TEST DETECTION EFFICIENCY ---------------------------

# Bubble chart - Tests vs Detected Cases Ratio
dataset1['DetectionEfficiency'] = dataset1['TotalCases'] / dataset1['TotalTests']

fig63 = px.scatter(dataset1.head(30),
                   x='TotalTests',
                   y='DetectionEfficiency',
                   hover_data=['Country/Region', 'Continent'],
                   color='DetectionEfficiency',
                   size='DetectionEfficiency',
                   size_max=80,
                   log_x=True)
fig63.show()


# --------------------------- STEP 34: RECOVERY BURDEN ---------------------------

# Bubble chart - ActiveCases vs TotalRecovered
fig64 = px.scatter(dataset1.head(30),
                   x='ActiveCases',
                   y='TotalRecovered',
                   hover_data=['Country/Region', 'Continent'],
                   color='TotalRecovered',
                   size='ActiveCases',
                   size_max=80,
                   log_x=True,
                   log_y=True)
fig64.show()


# --------------------------- STEP 35: POPULATION NORMALIZED SEVERITY ---------------------------

dataset1['Deaths_to_Cases'] = dataset1['TotalDeaths'] / dataset1['TotalCases']

fig65 = px.scatter(dataset1.head(30),
                   x='Cases/1M pop',
                   y='Deaths_to_Cases',
                   hover_data=['Country/Region', 'Continent'],
                   color='Deaths_to_Cases',
                   size='Deaths_to_Cases',
                   size_max=80)
fig65.show()


# --------------------------- STEP 36: HEALTHCARE LOAD DISTRIBUTION ---------------------------

fig66 = px.scatter(dataset1.head(30),
                   x='ActiveCases',
                   y='Serious/Critical',
                   hover_data=['Country/Region', 'Continent'],
                   color='ActiveCases',
                   size='Serious/Critical',
                   size_max=80,
                   log_x=True,
                   log_y=True)
fig66.show()


# --------------------------- STEP 37: TESTING COVERAGE VS ACTIVE CASES ---------------------------

fig67 = px.scatter(dataset1.head(30),
                   x='Tests/1M pop',
                   y='ActiveCases',
                   hover_data=['Country/Region', 'Continent'],
                   color='ActiveCases',
                   size='ActiveCases',
                   size_max=80,
                   log_x=True,
                   log_y=True)
fig67.show()


# --------------------------- STEP 38: CONTINENTAL BURDEN DISTRIBUTION ---------------------------

continent_sum = dataset1.groupby('Continent').sum(numeric_only=True).reset_index()

fig68 = px.scatter(continent_sum,
                   x='TotalCases',
                   y='TotalDeaths',
                   hover_data=['Continent'],
                   color='Continent',
                   size='TotalCases',
                   size_max=80,
                   log_x=True,
                   log_y=True)
fig68.show()


# --------------------------- STEP 39: CRITICAL CARE SHARE ---------------------------

dataset1['CriticalShare'] = dataset1['Serious/Critical'] / dataset1['TotalCases']

fig69 = px.scatter(dataset1.head(30),
                   x='CriticalShare',
                   y='DeathRate',
                   hover_data=['Country/Region', 'Continent'],
                   color='CriticalShare',
                   size='CriticalShare',
                   size_max=80)
fig69.show()


# --------------------------- STEP 40: GLOBAL OUTCOME BALANCE ---------------------------

fig70 = px.scatter(dataset1.head(30),
                   x='RecoveryRate',
                   y='DeathRate',
                   hover_data=['Country/Region', 'Continent'],
                   color='DeathRate',
                   size='RecoveryRate',
                   size_max=80)
fig70.show()
# --------------------------- STEP 41: CASE GROWTH PRESSURE ---------------------------

# New Cases vs Active Cases
fig71 = px.scatter(dataset1.head(30),
                   x='NewCases',
                   y='ActiveCases',
                   hover_data=['Country/Region', 'Continent'],
                   color='NewCases',
                   size='NewCases',
                   size_max=80,
                   log_y=True)
fig71.show()

# New Deaths vs Total Deaths
fig72 = px.scatter(dataset1.head(30),
                   x='NewDeaths',
                   y='TotalDeaths',
                   hover_data=['Country/Region', 'Continent'],
                   color='NewDeaths',
                   size='NewDeaths',
                   size_max=80,
                   log_y=True)
fig72.show()


# --------------------------- STEP 42: DAILY IMPACT INTENSITY ---------------------------

# New Cases per 1M vs New Deaths per 1M
fig73 = px.scatter(dataset1.head(30),
                   x='NewCases/1M pop',
                   y='NewDeaths/1M pop',
                   hover_data=['Country/Region', 'Continent'],
                   color='NewDeaths/1M pop',
                   size='NewCases/1M pop',
                   size_max=80)
fig73.show()

# New Cases vs Recovery Rate
fig74 = px.scatter(dataset1.head(30),
                   x='NewCases',
                   y='RecoveryRate',
                   hover_data=['Country/Region', 'Continent'],
                   color='RecoveryRate',
                   size='RecoveryRate',
                   size_max=80)
fig74.show()


# --------------------------- STEP 43: HEALTHCARE RESPONSE EFFECTIVENESS ---------------------------

# Serious/Critical vs Recovery Rate
fig75 = px.scatter(dataset1.head(30),
                   x='Serious/Critical',
                   y='RecoveryRate',
                   hover_data=['Country/Region', 'Continent'],
                   color='Serious/Critical',
                   size='Serious/Critical',
                   size_max=80,
                   log_x=True)
fig75.show()

# Active Ratio vs Recovery Rate
fig76 = px.scatter(dataset1.head(30),
                   x='ActiveRatio',
                   y='RecoveryRate',
                   hover_data=['Country/Region', 'Continent'],
                   color='ActiveRatio',
                   size='ActiveRatio',
                   size_max=80)
fig76.show()


# --------------------------- STEP 44: TESTING RESPONSE SPEED ---------------------------

# New Tests vs New Cases
fig77 = px.scatter(dataset1.head(30),
                   x='NewTests',
                   y='NewCases',
                   hover_data=['Country/Region', 'Continent'],
                   color='NewTests',
                   size='NewTests',
                   size_max=80)
fig77.show()

# New Tests per 1M vs New Cases per 1M
fig78 = px.scatter(dataset1.head(30),
                   x='NewTests/1M pop',
                   y='NewCases/1M pop',
                   hover_data=['Country/Region', 'Continent'],
                   color='NewTests/1M pop',
                   size='NewTests/1M pop',
                   size_max=80)
fig78.show()


# --------------------------- STEP 45: MORTALITY BURDEN TREND ---------------------------

# New Deaths vs Active Cases
fig79 = px.scatter(dataset1.head(30),
                   x='ActiveCases',
                   y='NewDeaths',
                   hover_data=['Country/Region', 'Continent'],
                   color='NewDeaths',
                   size='NewDeaths',
                   size_max=80,
                   log_x=True)
fig79.show()

# Deaths per 1M vs Critical Share
fig80 = px.scatter(dataset1.head(30),
                   x='Deaths/1M pop',
                   y='CriticalShare',
                   hover_data=['Country/Region', 'Continent'],
                   color='CriticalShare',
                   size='CriticalShare',
                   size_max=80)
fig80.show()


# --------------------------- STEP 46: RECOVERY MOMENTUM ---------------------------

# TotalRecovered vs RecoveryRate
fig81 = px.scatter(dataset1.head(30),
                   x='TotalRecovered',
                   y='RecoveryRate',
                   hover_data=['Country/Region', 'Continent'],
                   color='TotalRecovered',
                   size='TotalRecovered',
                   size_max=80,
                   log_x=True)
fig81.show()

# ActiveCases vs RecoveryRate (log scale)
fig82 = px.scatter(dataset1.head(30),
                   x='ActiveCases',
                   y='RecoveryRate',
                   hover_data=['Country/Region', 'Continent'],
                   color='RecoveryRate',
                   size='RecoveryRate',
                   size_max=80,
                   log_x=True)
fig82.show()


# --------------------------- STEP 47: POPULATION PRESSURE INDEX ---------------------------

dataset1['BurdenIndex'] = (
    dataset1['ActiveCases'] * 0.5 +
    dataset1['Serious/Critical'] * 0.3 +
    dataset1['NewCases'] * 0.2
)

fig83 = px.scatter(dataset1.head(30),
                   x='Population',
                   y='BurdenIndex',
                   hover_data=['Country/Region', 'Continent'],
                   color='BurdenIndex',
                   size='BurdenIndex',
                   size_max=80,
                   log_x=True)
fig83.show()


# --------------------------- STEP 48: PANDEMIC CONTROL SCORE ---------------------------

dataset1['ControlScore'] = (
    dataset1['RecoveryRate'] * 0.5 -
    dataset1['DeathRate'] * 0.3 -
    dataset1['Cases_per_Test'] * 0.2
)

fig84 = px.scatter(dataset1.head(30),
                   x='ControlScore',
                   y='SeverityIndex',
                   hover_data=['Country/Region', 'Continent'],
                   color='ControlScore',
                   size='ControlScore',
                   size_max=80)
fig84.show()


# --------------------------- STEP 49: CONTINENTAL RESPONSE BALANCE ---------------------------

continent_control = dataset1.groupby('Continent')['ControlScore'].mean().reset_index()

fig85 = px.scatter(continent_control,
                   x='Continent',
                   y='ControlScore',
                   color='ControlScore',
                   size='ControlScore',
                   size_max=80)
fig85.show()


# --------------------------- STEP 50: OVERALL PANDEMIC STABILITY ---------------------------

fig86 = px.scatter(dataset1.head(30),
                   x='ControlScore',
                   y='ActiveRatio',
                   hover_data=['Country/Region', 'Continent'],
                   color='ActiveRatio',
                   size='ActiveRatio',
                   size_max=80)
fig86.show()
# --------------------------- STEP 47: POPULATION PRESSURE INDEX ---------------------------

dataset1['BurdenIndex'] = (
    dataset1['ActiveCases'] * 0.5 +
    dataset1['Serious/Critical'] * 0.3 +
    dataset1['TotalDeaths'] * 0.2
)

fig83 = px.scatter(dataset1.head(30),
                   x='Country/Region',
                   y='BurdenIndex',
                   hover_data=['Country/Region', 'Continent'],
                   color='BurdenIndex',
                   size='BurdenIndex',
                   size_max=80)
fig83.show()
# --------------------------- STEP 47: ADVANCED BURDEN RELATIONSHIPS ---------------------------

# Bubble chart - TotalRecovered vs TotalDeaths
fig83 = px.scatter(dataset1.head(30),
                   x='TotalRecovered',
                   y='TotalDeaths',
                   hover_data=['Country/Region', 'Continent'],
                   color='TotalDeaths',
                   size='TotalRecovered',
                   size_max=80,
                   log_x=True,
                   log_y=True)
fig83.show()

# Bubble chart - TotalRecovered vs ActiveCases
fig84 = px.scatter(dataset1.head(30),
                   x='TotalRecovered',
                   y='ActiveCases',
                   hover_data=['Country/Region', 'Continent'],
                   color='ActiveCases',
                   size='ActiveCases',
                   size_max=80,
                   log_x=True)
fig84.show()


# --------------------------- STEP 48: TESTING INTENSITY ---------------------------

# Tests vs Population
fig85 = px.scatter(dataset1.head(30),
                   x='Population',
                   y='TotalTests',
                   hover_data=['Country/Region', 'Continent'],
                   color='TotalTests',
                   size='TotalTests',
                   size_max=80,
                   log_x=True,
                   log_y=True)
fig85.show()

# Tests vs ActiveCases
fig86 = px.scatter(dataset1.head(30),
                   x='TotalTests',
                   y='ActiveCases',
                   hover_data=['Country/Region', 'Continent'],
                   color='ActiveCases',
                   size='ActiveCases',
                   size_max=80,
                   log_x=True,
                   log_y=True)
fig86.show()


# --------------------------- STEP 49: RATE RELATIONSHIPS ---------------------------

# RecoveryRate vs ActiveRatio
fig87 = px.scatter(dataset1.head(30),
                   x='RecoveryRate',
                   y='ActiveRatio',
                   hover_data=['Country/Region', 'Continent'],
                   color='ActiveRatio',
                   size='RecoveryRate',
                   size_max=80)
fig87.show()

# DeathRate vs ActiveRatio
fig88 = px.scatter(dataset1.head(30),
                   x='DeathRate',
                   y='ActiveRatio',
                   hover_data=['Country/Region', 'Continent'],
                   color='DeathRate',
                   size='DeathRate',
                   size_max=80)
fig88.show()


# --------------------------- STEP 50: CASE DISTRIBUTION ---------------------------

# TotalCases vs Population
fig89 = px.scatter(dataset1.head(30),
                   x='Population',
                   y='TotalCases',
                   hover_data=['Country/Region', 'Continent'],
                   color='TotalCases',
                   size='TotalCases',
                   size_max=80,
                   log_x=True,
                   log_y=True)
fig89.show()

# Cases per 1M vs Population
fig90 = px.scatter(dataset1.head(30),
                   x='Population',
                   y='Cases/1M pop',
                   hover_data=['Country/Region', 'Continent'],
                   color='Cases/1M pop',
                   size='Cases/1M pop',
                   size_max=80,
                   log_x=True)
fig90.show()


# --------------------------- STEP 51: SEVERITY RELATIONSHIPS ---------------------------

# SeverityIndex vs TotalDeaths
fig91 = px.scatter(dataset1.head(30),
                   x='SeverityIndex',
                   y='TotalDeaths',
                   hover_data=['Country/Region', 'Continent'],
                   color='SeverityIndex',
                   size='SeverityIndex',
                   size_max=80,
                   log_y=True)
fig91.show()

# SeverityIndex vs ActiveCases
fig92 = px.scatter(dataset1.head(30),
                   x='SeverityIndex',
                   y='ActiveCases',
                   hover_data=['Country/Region', 'Continent'],
                   color='ActiveCases',
                   size='SeverityIndex',
                   size_max=80,
                   log_y=True)
fig92.show()

# SeverityIndex vs Population
fig93 = px.scatter(dataset1.head(30),
                   x='Population',
                   y='SeverityIndex',
                   hover_data=['Country/Region', 'Continent'],
                   color='SeverityIndex',
                   size='SeverityIndex',
                   size_max=80,
                   log_x=True)
fig93.show()
