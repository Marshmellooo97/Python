import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
df = pd.read_csv("C:/Users/justi/Documents/Codes/Pyton/Kursmaterialien-2019/Kursmaterialien/data/names.csv")
dfname = df[df["Name"] == "Anna"]
dfgeschlecht = dfname[dfname["Gender"] == "F"]
dfstate = dfgeschlecht[dfgeschlecht["State"] == "CA"]

df5 = dfstate.sort_values("Year")
print(dfstate)
plt.plot(df5["Year"], df5["Count"])
plt.show()


























