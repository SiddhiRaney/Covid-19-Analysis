# ------------------------------------------------------------
# Import required libraries
# ------------------------------------------------------------
import pandas as pd
import plotly.express as px

# ------------------------------------------------------------
# Step 1: Prepare the Dataset
# ------------------------------------------------------------
data = {
    'State': ['California', 'Texas', 'Florida', 'New York', 'Illinois'],
    'State_Code': ['CA', 'TX', 'FL', 'NY', 'IL'],
    'Population': [39538223, 29145505, 21538187, 20201249, 12812508]
}
df = pd.DataFrame(data)

# Output preview (expected when printing df):
#       State      State_Code   Population
# 0  California      CA         39538223
# 1  Texas           TX         29145505
# 2  Florida         FL         21538187
# 3  New York        NY         20201249
# 4  Illinois        IL         12812508

print(df)  # <-- This will show the above table

# ------------------------------------------------------------
# Step 2: Basic Choropleth Map
# ------------------------------------------------------------
fig = px.choropleth(
    df,
    locations='State_Code',      # Uses U.S. state codes
    locationmode='USA-states',   # Tells Plotly to treat them as U.S. states
    color='Population',          # Color intensity based on population
    hover_name='State',          # Shows full name on hover
    color_continuous_scale='Viridis',
    scope='usa',                 # Restrict view to U.S.
    title='U.S. State Population Estimates'
)

# Output: 
# ✅ An interactive U.S. map where darker shades represent higher populations.
# California will appear the darkest, Illinois the lightest.

fig.show()

# ------------------------------------------------------------
# Step 3: Improved Layout with Projection
# ------------------------------------------------------------
fig.update_layout(
    geo=dict(showframe=False, showcoastlines=True, projection_type='albers usa'),
    margin=dict(l=0, r=0, t=50, b=0)
)

# Output:
# ✅ Map becomes cleaner, with no frame and slightly warped to typical U.S. projection.

fig.show()

# ------------------------------------------------------------
# Step 4: Custom Color Variant (Blues)
# ------------------------------------------------------------
fig = px.choropleth(
    df,
    locations='State_Code',
    locationmode='USA-states',
    color='Population',
    hover_name='State',
    hover_data=['Population'],    # ✅ Shows exact number on hover
    color_continuous_scale='Blues',
    scope='usa',
    title='U.S. State Population Estimates (Blue Scale)'
)

# Output:
# ✅ Same as before but using a BLUE gradient instead of Viridis.
# Still interactive, hoverable.

fig.show()
fig.update_layout(
    coloraxis_colorbar=dict(
        title="Population",
        tickformat=",",        # Comma separated numbers
        len=0.75
    )
)

fig.show()
fig.update_traces(
    hovertemplate=
    "<b>%{hovertext}</b><br>" +
    "Population: %{z:,}<extra></extra>"
)

fig.show()
df["Population_M"] = df["Population"] / 1_000_000

fig = px.choropleth(
    df,
    locations="State_Code",
    locationmode="USA-states",
    color="Population_M",
    hover_name="State",
    hover_data={"Population_M": ":.2f"},
    color_continuous_scale="Viridis",
    scope="usa",
    title="U.S. State Population (in Millions)"
)

fig.update_layout(
    coloraxis_colorbar=dict(title="Population (M)")
)

fig.show()
# ------------------------------------------------------------
# Step 5: Add State Labels (Text Overlay)
# ------------------------------------------------------------
fig = px.choropleth(
    df,
    locations="State_Code",
    locationmode="USA-states",
    color="Population_M",
    hover_name="State",
    color_continuous_scale="Plasma",
    scope="usa",
    title="U.S. State Population with Labels (Millions)"
)

fig.update_traces(
    text=df["State_Code"],   # show state codes
    texttemplate="%{text}",
    textfont_size=10
)

fig.update_layout(
    coloraxis_colorbar=dict(title="Population (M)")
)

fig.show()


# ------------------------------------------------------------
# Step 6: Discrete Population Categories (Binned Choropleth)
# ------------------------------------------------------------
df["Pop_Category"] = pd.cut(
    df["Population_M"],
    bins=[0, 15, 25, 35, 45],
    labels=["Low", "Medium", "High", "Very High"]
)

fig = px.choropleth(
    df,
    locations="State_Code",
    locationmode="USA-states",
    color="Pop_Category",
    hover_name="State",
    hover_data=["Population_M"],
    scope="usa",
    title="U.S. States by Population Category",
    color_discrete_sequence=px.colors.qualitative.Set2
)

fig.show()


# ------------------------------------------------------------
# Step 7: Side-by-Side Comparison Using Facets
# ------------------------------------------------------------
df_long = df.melt(
    id_vars=["State", "State_Code"],
    value_vars=["Population", "Population_M"],
    var_name="Metric",
    value_name="Value"
)

fig = px.choropleth(
    df_long,
    locations="State_Code",
    locationmode="USA-states",
    color="Value",
    hover_name="State",
    facet_col="Metric",
    scope="usa",
    color_continuous_scale="Viridis",
    title="Population Comparison: Absolute vs Millions"
)

fig.update_layout(margin=dict(t=60, l=0, r=0, b=0))
fig.show()


# ------------------------------------------------------------
# Step 8: Add Custom Hover Styling
# ------------------------------------------------------------
fig = px.choropleth(
    df,
    locations="State_Code",
    locationmode="USA-states",
    color="Population_M",
    hover_name="State",
    scope="usa",
    title="Enhanced Hover Tooltip"
)

fig.update_traces(
    hovertemplate=
    "<b>%{hovertext}</b><br>" +
    "Population (M): %{z:.2f}<br>" +
    "<extra></extra>"
)

fig.show()


# ------------------------------------------------------------
# Step 9: Export Map to HTML (For Submission / Portfolio)
# ------------------------------------------------------------
fig.write_html("us_population_choropleth.html")
# ------------------------------------------------------------
# Step 10: Animated Choropleth (Simulated Year-wise Growth)
# ------------------------------------------------------------
# Create fake population growth over years for animation
years = [2015, 2018, 2021, 2024]

df_anim = pd.concat([
    df.assign(Year=year, Population_M=df["Population_M"] * (1 + 0.02 * i))
    for i, year in enumerate(years)
])

fig = px.choropleth(
    df_anim,
    locations="State_Code",
    locationmode="USA-states",
    color="Population_M",
    hover_name="State",
    animation_frame="Year",
    color_continuous_scale="Viridis",
    scope="usa",
    title="Animated U.S. State Population Growth (Simulated)"
)

fig.update_layout(
    coloraxis_colorbar=dict(title="Population (M)")
)

fig.show()


# ------------------------------------------------------------
# Step 11: Highlight Top-N States (Conditional Coloring)
# ------------------------------------------------------------
# Rank states by population
df["Rank"] = df["Population"].rank(ascending=False)

fig = px.choropleth(
    df,
    locations="State_Code",
    locationmode="USA-states",
    color=df["Rank"] <= 3,   # Top 3 states highlighted
    hover_name="State",
    hover_data=["Population"],
    scope="usa",
    title="Top 3 Most Populous U.S. States Highlighted",
    color_discrete_map={True: "red", False: "lightgrey"}
)

fig.show()


# ------------------------------------------------------------
# Step 12: Dark Mode Map (Dashboard Ready)
# ------------------------------------------------------------
fig = px.choropleth(
    df,
    locations="State_Code",
    locationmode="USA-states",
    color="Population_M",
    hover_name="State",
    color_continuous_scale="Turbo",
    scope="usa",
    title="U.S. Population Choropleth (Dark Mode)"
)

fig.update_layout(
    template="plotly_dark",
    coloraxis_colorbar=dict(title="Population (M)")
)

fig.show()


# ------------------------------------------------------------
# Step 13: Add Annotations (Insight Text on Map)
# ------------------------------------------------------------
fig = px.choropleth(
    df,
    locations="State_Code",
    locationmode="USA-states",
    color="Population_M",
    hover_name="State",
    scope="usa",
    title="U.S. Population with Insights"
)

fig.add_annotation(
    text="California is the most populous state",
    x=0.02, y=0.1,
    xref="paper", yref="paper",
    showarrow=False,
    font=dict(size=12)
)

fig.show()


# ------------------------------------------------------------
# Step 14: Combine Choropleth + Bar Chart (Dashboard Feel)
# ------------------------------------------------------------
from plotly.subplots import make_subplots
import plotly.graph_objects as go

fig = make_subplots(
    rows=1, cols=2,
    specs=[[{"type": "choropleth"}, {"type": "bar"}]],
    subplot_titles=("Population Map", "Population Ranking")
)

fig.add_trace(
    go.Choropleth(
        locations=df["State_Code"],
        locationmode="USA-states",
        z=df["Population_M"],
        text=df["State"],
        colorscale="Viridis",
        colorbar_title="Population (M)"
    ),
    row=1, col=1
)

fig.add_trace(
    go.Bar(
        x=df.sort_values("Population_M", ascending=False)["State"],
        y=df.sort_values("Population_M", ascending=False)["Population_M"]
    ),
    row=1, col=2
)

fig.update_geos(scope="usa")
fig.update_layout(title_text="U.S. Population Dashboard View")
fig.show()


# ------------------------------------------------------------
# Step 15: Save Final Dashboard
# ------------------------------------------------------------
fig.write_html("us_population_dashboard.html")

