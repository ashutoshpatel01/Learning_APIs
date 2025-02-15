import pandas as pd
import requests

# API Endpoint (replace with actual API URL)
url = "https://api.freeapi.app/api/v1/public/randomproducts"

# Fetch API Response
response = requests.get(url)
data = response.json()

# Extract product list
products = data["data"]["data"]  # Access nested "data" inside "data"

# Convert JSON to Pandas DataFrame
df = pd.DataFrame(products)

# Display the table
print(df)
