import pandas as pd
dict = {
    "name":["yhd","yh","y"],
    "age":[23,11,23],
    "location":["kamonyi","kirehe","ngoma"],
     "Money":[0 ,0,0] }
df = pd.DataFrame(dict)
print (df)

import numpy

ages = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]

x = numpy.percentile(ages, 90)

print(x)