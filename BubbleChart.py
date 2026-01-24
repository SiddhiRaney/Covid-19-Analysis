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
