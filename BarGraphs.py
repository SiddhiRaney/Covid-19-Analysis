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
