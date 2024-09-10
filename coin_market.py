import requests
import pandas as pd

# Your API key from CoinMarketCap
api_key = 'f7288dd6-166b-4e1c-8b54-da9d33c2a901'

# API endpoint for cryptocurrency listings
url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': api_key,
}

params = {
    'start': '1',
    'limit': '1000',
    'convert': 'USD'
}

# Step 1: Send GET request to the API
response = requests.get(url, headers=headers, params=params)
data = response.json()
#json --> dict
#print(data)

# Step 2: Normalize the JSON data to pandas DataFrame
df = pd.json_normalize(data['data'])

# Step 3: Save to CSV
df.to_excel('coinmarketcap_api_data1000.xlsx', index=False)

# Optional: Print first 5 rows
print(df.head())


''' change column two's name as 'block chain name'
    compute market cap by creating new column : circulating_supply * price
    categorization columns-- small, mid, large cap
    remove unnecessary column
'''
