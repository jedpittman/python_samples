# . How Do You Keep Only the Top Two Most Frequent Values as It Is and Replace Everything Else as ‘other’ in a Series?
#Input
import pandas as pd
import numpy as np
np.random.RandomState(100)

ser = pd.Series(np.random.randint(1, 5, [12]))

#Solution
print("Top 2 Freq:", ser.value_counts())
ser[~ser.isin(ser.value_counts().index[:2])] = 'Other’
print(ser)

# How Do You Find the Positions of Numbers That Are Multiples of Three from a Series?
>> #Input
import pandas as pd
ser = pd.Series(np.random.randint(1, 10, 7))
ser

#Solution
print(ser)
np.argwhere(ser % 3==0)

# How do you reverse the rows of a dataframe df?
df.iloc[::-1, :]


# What are the key features of the Python 3.9.0.0 version?
# Zoneinfo and graphlib are two new modules.
# Improved modules such as asyncio and ast.
# Optimizations include improved idiom for assignment, signal handling, and Python built-ins.
# Removal of erroneous methods and functions.
# Instead of LL1, a new parser is based on PEG.
# Remove Prefixes and Suffixes with New String Methods.
# Generics with type hinting in standard collections.