# import pandas as pd
# import numpy as np
# data = pd.Series([1, np.nan,3.5,np.nan,7])
# print(data.dropna)

import pandas as pd
import numpy as np

data = {
    'Name': ['Mona' , 'Nidhi'],
    'Marks':['98' , '58']
}
df = pd.DataFrame(data)
print(df)

