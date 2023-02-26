from string import ascii_letters,digits
from random import choices
import re

def gnerate_password():
    global passwd
    global match
    digitos=int(input('Insira quantos digitos:'))
    c=ascii_letters+digits+'#%&*+-@*?%#@*:'
    passwd=''.join(choices(c,k=digitos))
    rgx=['\W','[a-z]','[A-Z]','\d']
    match=list(filter(lambda x:re.search(r''+x+'',passwd),rgx))
gnerate_password()

while True:
    if len(match)==4:
        print(passwd)
        break
    else:
        gnerate_password()