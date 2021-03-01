import pandas as pd

data = pd.read_csv("202009020838.csv")
data.columns = [column.replace(" ", "_") for column in data.columns]
x = data["total"].between(245, 345, inclusive=True)
print(data)
