import requests
import hashlib
from bs4 import BeautifulSoup
url = 'http://docker.hackthebox.eu:39664/'
session = requests.session()
target_response = session.get(url)
soup_obj = BeautifulSoup(target_response.text,'html.parser')
plain_text = soup_obj.h3.text
cipher_text = hashlib.md5(plain_text.encode())
post_param = {'hash' : cipher_text.hexdigest()}
final_res = session.post(url, post_param)
print(final_res.text)

