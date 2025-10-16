import pandas as pd

# i. Create and display a one-dimensional array-like object (Pandas Series)
data = pd.Series([10, 20, 30, 40, 50])
print("Pandas Series:")
print(data)

# ii. Convert the Pandas Series to a Python list and display its type
data_list = data.tolist()
print("\nSeries converted to list:")
print(data_list)
print("Type of the list:", type(data_list))
