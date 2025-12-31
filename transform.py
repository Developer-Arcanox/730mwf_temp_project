import pandas as pd

# Sample DataFrame
data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "Salary": [50000, 60000, 70000],
}

df = pd.DataFrame(data)

df["Bonus"] = df["Salary"] * 0.1

df["Total Salary"] = df["Salary"] + df["Bonus"]

# df.drop(columns=["Bonus", "Salary"], inplace=True)


def checkGrade(n):
    if n > 100000:
        return "A"
    elif n > 60000:
        return "B"
    else:
        return "C"


df["Grade"] = df["Salary"].apply(checkGrade)

df["Length"] = df["Name"].map(len)

df[["Age", "Salary"]] = df[["Age", "Salary"]].applymap(lambda x: x + 1)

print(df)
