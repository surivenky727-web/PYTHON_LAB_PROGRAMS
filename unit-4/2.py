import pandas as pd
import numpy as np

# Sample data and labels
exam_data = {
    'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
    'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
    'attempts': [1, 3, 2, 3, 1, 1, 2, 1, 2, 1],
    'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']
}
labels = ['a','b','c','d','e','f','g','h','i','j']

# i) Create and display DataFrame
df = pd.DataFrame(exam_data, index=labels)
print("DataFrame:\n", df)

# ii) Change 'James' to 'Suresh' in 'name' column
df['name'] = df['name'].replace('James', 'Suresh')
print("\nAfter replacing James with Suresh:\n", df)

# iii) Insert a new column in existing DataFrame
df['country'] = ['USA', 'UK', 'USA', 'UK', 'USA', 'UK', 'USA', 'UK', 'USA', 'UK']
print("\nAfter inserting new column 'country':\n", df)

# iv) Get list from DataFrame column headers
column_list = list(df.columns)
print("\nList of column headers:", column_list)

# v) Get list from DataFrame column headers (duplicate step)
column_list2 = list(df.columns)
print("\nList of column headers (again):", column_list2)
