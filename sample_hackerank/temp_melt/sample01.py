import pandas as pd

#Create a pandas dataframe with months, temperatures and cities.
data = {'Month': ['January', 'February', 'March', 'April', 'May', 'June'],
    'Temperature': [32, 45, 60, 70, 80, 90],
    'City': ['Boston', 'Seattle', 'Miami', 'Boston', 'Seattle', 'Miami']}
df = pd.DataFrame(data)

print('input', df)
print('output', pd.pivot_table(df, index='Month', columns='City', values='Temperature', aggfunc='max').reset_index())
#make a column called month into the index for the dataframe.