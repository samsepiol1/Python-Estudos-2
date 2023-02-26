import requests
import time
lista_urls = ["https://portal.ifrn.edu.br/"]
def download_image(lista_url):
    img_bytes = requests.get(lista_url).content
    img_name = lista_url.split('/')[3]
    img_name = f'{img_name}.jpg'
    with open(img_name, 'wb') as img_file:
        img_file.write(img_bytes)
        print(f'{img_name} was downloaded...')

for _ in range(5):
    download_image('https://portal.ifrn.edu.br/')

