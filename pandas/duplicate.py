import pandas as pd
import numpy as np

data = pd.Series([1,-999,3.5,-1000,7])
print(data)
replaced = data.replace({-999 : np.nan, -1000:0})
print("replaced\n" , replaced)

