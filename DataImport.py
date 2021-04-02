import pandas as pd

data = pd.read_csv("netflix_titles.csv")

#print(data.info())

# count the number of missing values in each column
# missing_values_count = data.isnull().sum()

# print(missing_values_count)

#Drop rows where data is missing
# droprows = data.dropna(axis=1)

#Adding axis= drops columns instead of rows

# print(data.shape,droprows.shape)

#Better to fill values instead of dropping them


new_data = data.fillna("null")
missing_values = new_data.isnull().sum()
print(data.shape,new_data.shape)
print(missing_values)

#There are now no missing values as all blanks have been filled with null


