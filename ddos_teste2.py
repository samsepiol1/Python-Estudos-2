import requests
import time

def enviando_requsicao(site):
    for x in range(1,2000):
        r=requests.get(site)

        print(r.status_code)
    for y in range(1,2000):
        r=requests.get(1,2000)
        print("segundo teste"+r.status_code)
enviando_requsicao('http://app-auxilio.online')


