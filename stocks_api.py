import requests
import pandas as pd

url = "https://api.freeapi.app/api/v1/public/stocks/INFY"
def get_stock():
# Fetch API Response
  response = requests.get(url)
  data = response.json()

# Extract product list
  print(list(data.values()))# Access nested "data" inside "data"

  for key, value in data.items():
    print(f"{key}: {value}")

  df = pd.DataFrame([data])

# Print table
  print(df)

def main():
  try:
    get_stock()

  except Exception as e:
    print(str(e))
if __name__ == "__main__":
  main()

