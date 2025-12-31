import pandas as pd

data = {
    "Department": ["HR", "IT", "HR", "IT", "Finance", "HR"],
    "Employee": ["Alice", "Bob", "Charlie", "David", "Eve", "Alice"],
    "Salary": [50000, 60000, 55000, 65000, 70000, 200],
}


df = pd.DataFrame(data)

# df_pivot = df.pivot_table(
#     index="Employee", columns="Department", values="Salary", aggfunc="sum"
# )

# print(df_pivot)

df_crosstab = pd.crosstab(df["Department"], df["Employee"])
print("Hello")
