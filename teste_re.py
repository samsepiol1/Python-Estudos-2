import requests

url = "https://www.tecmundo.com.br/"

res = requests.get(url)
for items in res.json()['nzn-mosaic-news']:
    print(items['Title'])