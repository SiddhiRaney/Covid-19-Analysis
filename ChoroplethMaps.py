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

