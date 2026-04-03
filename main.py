##ES main file 
#
##make a funtio for main 
#from faker import Faker
#fake = Faker()
#print(fake.profile())
#
#from faker import Faker 
#
#fake = Faker('EN_US')      
#
#for i in range(0,2): 
#    print('Name->', fake.name(),"\n",'Country->', fake.country())
#
#import matplotlib.pyplot as plt
#import numpy as np
#
#xpoints = np.array([1, 8])
#ypoints = np.array([3, 10])
#
#plt.plot(xpoints, ypoints)
#plt.show()
#
#import pandas as pd
#from faker import Faker
#
#fake = Faker()
#
## Generate a list of 100 fake user records
#data = [
#    {
#        "Name": fake.name_female(),
#        "Email": fake.email(),
#        "Address": fake.address(),
#        "Join Date": fake.date_this_decade()
#    }
#    for _ in range(3)
#]

#df = pd.DataFrame(data)
 
# Preview the results
#print(df.head())

import pandas as pd

pd.index = pd.index + 1


calories = [{"day1": 420, "day2": 380, "day3": 390}]

myvar = pd.DataFrame(calories)

print(myvar)
