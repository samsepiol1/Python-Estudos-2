import PyPDF2
import string
def horario():
 pergunta=input('Deseja iniciar o programa S/N').upper()
 while pergunta=='S':
  linha2=input('De qual Linha você quer saber os horarios').upper()
  if linha2=='A':
   f=open('teste.txt','r')
   texto=f.read()
   print(texto)
   texto_fechar = f.close()
  elif linha2=='B':
    f=open('testeB.txt','r')
    texto=f.read()
    print(texto)
    texto_fechar = f.close()
  elif linha2=='C':
    f=open('testeC.txt','r')
    texto=f.read()
    print(texto)
    texto_fechar = f.close()
  elif linha2=='G':
    f=open('testeG.txt','r')
    texto=f.read()
    print(texto)
  elif linha2=='H':
    f=open('testeH.txt','r')
    texto=f.read()
    print(texto)
    texto_fechar = f.close()
  elif linha2=='J':
    f=open('testeJ.txt','r')
    texto=f.read()
    print(texto)
    texto_fechar = f.close()
  elif linha2=='L':
    f=open('testeL.txt','r')
    texto=f.read()
    print(texto)
    texto_fechar = f.close()
  elif linha2=='M':
    f=open('testeM.txt','r')
    texto=f.read()
    print(texto)
    texto_fechar = f.close()
  elif linha2=='N':
    f=open('testeN.txt','r')
    texto=f.read()
    print(texto)
    texto_fechar = f.close()
  elif linha2=='P':
    f=open('testeP.txt','r')
    texto=f.read()
    print(texto)
    texto_fechar = f.close()
  elif linha2=='V':
    f=open('testeV.txt','r')
    texto=f.read()
    print(texto)
    texto_fechar = f.close()











