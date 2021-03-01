import pandas as pd

data = pd.read_csv("202009020838.csv")
data.columns = [column.replace(" ", "_") for column in data.columns]
data.query('total == 345', inplace=True)
print(data)
