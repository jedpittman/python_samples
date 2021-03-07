import pandas as pd
import numpy as np
import requests
from pypfopt.efficient_frontier import EfficientFrontier
from pypfopt import risk_models
from pypfopt import expected_returns

#load the data
# from google.colab import files
# files.upload()

# Store the data
df = pd.read_csv("data\FakeStockData.csv")
# df = pd.read_csv('NUSE_Close.csv')
#df # show the data frame.
# Should be this form:
# Date | Symbol1 | symbol2 ... etc.
# for each symbol, should be a close price.

# Set the date as the index
df.set_index(pd.DatetimeIndex(df['Date'].values))

# Remove the date column from the df
# columns = axis 1
df.drop(columns=['Date'], axis=1, inplace=True)
#print(df)
#df
#exit(1)



# Calculate the expected annualized returns and the annualized
# sample covariance matrix of the daily asset returns.
mu = expected_returns.mean_historical_return(df)
S = risk_models.sample_cov(df)

# SR describes the excess return you get for volitility you endure holding
# a riskier asset. 

ef = EfficientFrontier(mu, S) # create the EF object
weights = ef.max_sharpe() # Get the raw weights

# this will set weights below cutoff to zero, rounding the rest.
cleaned_weights = ef.clean_weights()
print(cleaned_weights)


#show the expected return, SR, and 
# in a jupyter notebook, this shows an ordered dicts.
# should sum to 1 for all weights.
ef.portfolio_performance(verbose=True)


#Figure out the allocations for each stock.
# pip install pulp

#Get the discrete allocation of each share per stock
from pypfopt.discrete_allocation import DiscreteAllocation, get_latest_prices

portfolio_val = 5000 # how much to invest
latest_prices = get_latest_prices(df)
weights = cleaned_weights
da = DiscreteAllocation(weights, latest_prices, total_portfolio_value=portfolio_val)
allocation, leftover = da.lp_portfolio()

# Returns a dictionary with pairs ticker: #shares
# Returns 1 leftover.
print('Discrete allocation:', allocation)
print("leftovers: ",leftover)
exit(1)
"""
# Get company name for stock ticker
def get_company_name(symbol):
    url = 'http://d.yimg.com/autoc.finance.yahoo.com/autoc?query=' + symbol + '&region=1lang=en'
    result = requests.get(url).json()
    for r in result['ResultSet']['Result']:
        if r['symbol'] == symbol:
            return r['name']

# Store the company name into a list.
company_name = []
for symbol in allocation: 
    company_name.append( get_company_name(symbol))

# Get the discrete allocation values
discrete_allocation_list = []
for symbol in allocation:
    discrete_allocation_list.append(allocation.get(symbol)

# Create a dataframe for the portfolio
portfolio_df = pd.DataFrame(columns=['Company_name', 'Company_ticker', 'Discrete_val_' + str(portfolio_val)])
portfolio_df['Company_name'] = company_name
portfolio_df['Company_ticker'] = allocation
portfolio_df['Discrete_val' + str(portfolio_val)] = discrete_allocation_list

# Show it.
portfolio_df

"""