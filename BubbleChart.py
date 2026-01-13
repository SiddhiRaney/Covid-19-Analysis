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
