# import numpy as np
# x = np.array([1,2,3,4,5,6,7,8])
# for i in x:
#     print(i)

import numpy as np
arr = np.array([1,2,3])
for idx, x in np.nenumerate(arr):
    print(idx, x)