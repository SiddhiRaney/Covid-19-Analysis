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
