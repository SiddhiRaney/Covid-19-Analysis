# Step 3: Dataset Cleaning

# View column labels of dataset1
print(dataset1.columns)

# Drop unnecessary columns with NaN values
dataset1.drop(['NewCases', 'NewDeaths', 'NewRecovered'], axis=1, inplace=True)

# Display a random sample of 5 rows
print(dataset1.sample(5))

# Create a table using Plotly Express
from plotly.figure_factory import create_table

colorscale = [[0, '#4d004c'], [.5, '#f2e5ff'], [1, '#ffffff']]
table = create_table(dataset1.head(15), colorscale=colorscale)

import plotly.offline as py
py.iplot(table)
