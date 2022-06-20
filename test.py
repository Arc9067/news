from email import header
import requests
import json
import urllib

headers = {"Content-type": "application/json", "x-api-key": "BfJyz9j2ubYvdUdU39ofVpOCrEGygVt0RxyME2nMjAlKd4QAC6fUtiqAg5AgjsD7"}

url = "https://deep-index.moralis.io/api/v2/erc20/0xddBB3a280D140Fb1241885857497A2E1d1A596Ac/price?chain=bsc"

response = requests.get(url, headers=headers)
print(response.json())