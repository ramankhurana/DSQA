import pandas as pd

# Example DataFrame
data = {
    'ID': [1, 1, 2, 2, 3, 3, 3],
    'Category': ['A', 'NA', 'B', 'C', 'NA', 'C', 'D']
}
df = pd.DataFrame(data)

# Create a binary indicator for 'NA'
df['NA_Indicator'] = (df['Category'] == 'NA').astype(int)

# Create dummy variables for each category, except 'NA'
dummies = pd.get_dummies(df['Category'])
dummies = dummies.drop('NA', axis=1, errors='ignore')  # Drop the 'NA' dummy column if exists

# Sum up the dummies for each ID
category_sum = dummies.groupby(df['ID']).sum()

# Sum the 'NA' indicator for each ID
na_sum = df.groupby('ID')['NA_Indicator'].max()  # Using max to ensure 1 if any 'NA' present

# Join the summed categories and the 'NA' indicator on ID
result_df = pd.concat([na_sum, category_sum], axis=1).reset_index()

print(result_df)


## new functionality 

import pandas as pd

# Sample DataFrame
data = {
    'Category': ['A', 'A', 'B', 'B', 'C', 'C', 'C'],
    'Values': [0, 1, 0, 0, 2, 0, 0]
}

df = pd.DataFrame(data)

# Group by 'Category' and count zeros in 'Values' column
zero_counts = df.groupby('Category')['Values'].apply(lambda x: (x == 0).sum()).reset_index()

# Rename the column for clarity
zero_counts.columns = ['Category', 'ZeroCount']

print(zero_counts)
