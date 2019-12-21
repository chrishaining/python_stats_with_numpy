import pandas as pd
import numpy as np

df1 = pd.DataFrame({
'name': ["Alice", "Sandy", "Nev", "Varda"],
'age': [32, 21, 104, 60]
})
print(df1)


df2 = pd.DataFrame([
['bike', 'red', 50],
['car', 'silver', 180],
['jet', 'black', 30000]
],
columns=['vehicle', 'colour', 'speed (mph)']
)
print(df2)
