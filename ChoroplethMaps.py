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
