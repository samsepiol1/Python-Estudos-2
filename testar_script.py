import requests
i
r = requests.get('https://suap.ifrn.edu.br/media/fotos/75x100/4237.dsoKFwDWnBh4.jpg')
print(r.headers.get('content-type'))
variavel =
open(variavel +'dsoKFwDWnBh4.jpg','wb').write(r.content)

