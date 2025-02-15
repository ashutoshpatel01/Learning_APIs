import requests
import pandas as pd

url = "https://api.freeapi.app/api/v1/public/randomproducts"
max_page = 4
def fetch_watch_data():
  
   for pg in range(1, max_page+1):#only printing for pages from all responses
      querystring = {"page":str(pg),"limit":"2","inc":"category%2Cprice%2Cthumbnail%2Cimages%2Ctitle%2Cid","query":"mens-watches and price >= 46 and price <= 180"}

   headers = {"accept": "application/json"}

   response = requests.get(url, headers=headers, params=querystring)
   data = response.json()

   df = pd.DataFrame(data)
   print(df.head(3))
fetch_watch_data()