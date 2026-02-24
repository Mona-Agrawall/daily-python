import pandas as pd
data = {
    'Name':['Mona' , 'Nidhi'],
    'Marks' :[22,33]
}

df = pd.DataFrame(data)
print(df)
print(df.loc[:, 'Name'])
