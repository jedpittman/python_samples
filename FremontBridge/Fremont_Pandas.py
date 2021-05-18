import pandas as pd

#Load a csv.
data = pd.read_csv('FremontBridge.csv', index_col='Date', parse_dates=True)

#Rename Columns
data.columns = ['Total', 'West','East'] #Shorten Column Names
print(data.index.hour)
#exit(end="finished",flush=True)

#Create a new column with Eval

data["EWDiff"] = data.eval('abs(West - East)')
data["Hour"] = data.index.hour
data["Weekday"] = data.index.weekday
data["Month"] = data.index.month
#Show the head
print(data.head())

#Drop the NAs and give a set of descriptive statistics: 
#mean,std,min,25/50/75%,max
print(data.dropna().describe())

