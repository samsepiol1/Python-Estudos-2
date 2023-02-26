""""
import Algorithmia

input={
    "image": "data://.algo/deeplearning/ColorfulImageColorization/perm/17883134_329570274124953_8213051817366388736_a.jpg"
}

client=Algorithmia.client('simzg4/ToRVWhuAKOvAVCgqrvjD1')

algo=client.algo('deeplearning/ColorfulImageColorization/1.1.13')

algo.set_options(timeout=300)

print(algo.pipe(input).result)
"""
import Algorithmia
import re
import unicodedata
input="data://.algo/util/SmartImageDownloader/perm/Screenshot_20200226-142106.png"

client=Algorithmia.client('simzg4/ToRVWhuAKOvAVCgqrvjD1')

algo = client.algo('ocr/RecognizeCharacters/0.3.0')

algo.set_options(timeout=300)



informacao_pessoa=algo.pipe(input).result

def removerAcentos(palavra):
    nfkd=unicodedata.normalize('NFKD',palavra)
    palavra_SemAcento=u"".join([c for c in nfkd if not unicodedata.combining(c)])

    return re.sub('[^a-zA-Z0-9 \\\]', '', palavra_SemAcento)
print(removerAcentos(informacao_pessoa).lstrip())
print(len(informacao_pessoa))





