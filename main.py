import pandas as pd

# Sample DataFrame
# data = {
#     "Department": ["HR", "IT", "HR", "IT", "Finance"],
#     "Employee": ["Alice", "Bob", "Charlie", "David", "Eve"],
#     "Salary": [50000, 60000, 55000, 65000, 70000],
# }

# df = pd.DataFrame(data)

# print(df)

# department = df.groupby(["Department", "Employee"])["Salary"].sum()

# aggregate = df.groupby("Department").agg(
#     {"Salary": ["sum", "mean"], "Employee": "count"}
# )

# print(aggregate)

# df1 = pd.DataFrame({"ID": [1, 2, 3], "Name": ["Alice", "Bob", "Charlie"]})
# df2 = pd.DataFrame({"ID": [1, 2, 4], "Salary": [50000, 60000, 70000]})

# join = pd.merge(df1, df2, on="ID", how="right")

# print(join)


# df1 = df1.set_index("ID")
# df2 = df2.set_index("ID")

# join = df1.join(df2, how="outer")

# print(join)
