# Step 1: Import required library
import pandas as pd

# Step 2: Importing the Datasets

# Importing Dataset1: covid.csv
covid = pd.read_csv("covid.csv")
print("First 5 rows of covid dataset:")
print(covid.head())

# Dataset1 shape and size
print("\ncovid dataset shape:", covid.shape)
print("covid dataset size:", covid.size)

# Dataset1 concise info
print("\ncovid dataset info:")
covid.info()

# Importing Dataset2: covid_grouped.csv
covid_grouped = pd.read_csv("covid_grouped.csv")
print("\nFirst 5 rows of covid_grouped dataset:")
print(covid_grouped.head())

# Dataset2 shape and size
print("\ncovid_grouped dataset shape:", covid_grouped.shape)
print("covid_grouped dataset size:", covid_grouped.size)

# Dataset2 concise info
print("\ncovid_grouped dataset info:")
covid_grouped.info()

# Importing Dataset3: coviddeath.csv
coviddeath = pd.read_csv("coviddeath.csv")
print("\nFirst 5 rows of coviddeath dataset:")
print(coviddeath.head())

# Dataset3 shape and size
print("\ncoviddeath dataset shape:", coviddeath.shape)
print("coviddeath dataset size:", coviddeath.size)

# Dataset3 concise info
print("\ncoviddeath dataset info:")
coviddeath.info()
