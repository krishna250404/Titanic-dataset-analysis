import numpy as np
import pandas as pd

df = pd.read_csv("Titanic.csv")


print("=======================================================")
df.fillna({"Age":df['Age'].median(), "Embarked":df["Embarked"].mode(), "Cabin":"unkown"}, inplace=True)
# df.to_csv("new.csv")
df["Ticket"] = pd.to_numeric(df["Ticket"], errors='coerce')
print(df)