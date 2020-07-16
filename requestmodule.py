import requests

r= requests.get("https://financialmodelingprep.com/api/v3/stock/real-time-price/AAPL")

print(r.text)

url="www.something.com"
data={"p":4,"p2":5}

r2=requests.post(url=url,data=data)