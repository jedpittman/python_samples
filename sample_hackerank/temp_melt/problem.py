import pandas as pd
# in a pandas dataframe df, make a column called month into the index for the dataframe.
# then melt the dataframe so that the columns are the cities and the values are the temperatures.
# print the resulting dataframe.


import pandas as pd

# load the data from temperture.csv
weather = pd.read_csv('temperature.csv')
# print the data
print(weather)


def pivotTable(weather: pd.DataFrame) -> pd.DataFrame:
    full_df = pd.DataFrame()
    cities = sorted(weather['city'].drop_duplicates().to_list())
    for c in cities:
        city_df = weather[weather['city']==c]
        city_df = city_df.rename(columns={'temperature':c})
        del city_df['city']
        city_df.sort_values(['month'], inplace=True, ignore_index=True)
        if len(full_df) == 0:
            full_df = city_df
        else:
            full_df = pd.concat([full_df, city_df[[c]]], join='inner', axis=1)
    full_df.set_index(['month'], inplace=True)
    return full_df

print(pivotTable(weather))