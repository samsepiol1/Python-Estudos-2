import urllib.request
import random
for c in range(51):
    # Adding information about user agent
    opener = urllib.request.build_opener()
    opener.addheaders = [('User-Agent',
                          'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
    urllib.request.install_opener(opener)

    # setting filename and image URL
    if c < 10:
        image_url = "https://readcomicsonline.ru/uploads/manga/batman-three-jokers-2020/chapters/1/" + "0" + str(
            c) + ".jpg"
        filename = str(c)+".jpg"
        try:
            urllib.request.urlretrieve(image_url, filename)
            print('200')
        except Exception as e:
            print('404')
        print(image_url)
    elif c >= 10:
        image_url = "https://readcomicsonline.ru/uploads/manga/batman-three-jokers-2020/chapters/1/" + str(c) + ".jpg"
        filename = str(c) + ".jpg"
        try:
            urllib.request.urlretrieve(image_url, filename)
            print('200')
        except Exception as e:
            print('404')

    # calling urlretrieve function to get resource

