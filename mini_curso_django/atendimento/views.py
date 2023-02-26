import datetime
from django.shortcuts import render
from django.template import Template,Context,loader
from django.http import HttpResponse


# Create your views here.

#Criando uma View

#Exemplo de controle que retorna como resposta um texto simples

def index(request):
    return HttpResponse("Está tudo bem por aqui")

#Exemplo de controle que retorna um html simples

def index2(request):
    html='<html><body style="color:red"> Está tudo bem por aqui</body></html>'
    return HttpResponse(html)

def index3(request):
    now=datetime.datetime.now()

    template=Template('<html><body>Tudo bem por aqui {{current_date}}.</body></html>')

    #Conjunto de variáveis que vão ser processadas pelo template
    context=Context({'current_date':now})
    html=template.render(context)
    return HttpResponse(html)

def index4a(request):
    template=loader.get_template('atendimento/index4.html')
    context={
        'current_date:':datetime.datetime.now(),

    }
    return HttpResponse(template.render(context,request))
def index4b(request,idade=None):
    current_date=datetime.datetime.now()

    return render(request,'atendimento/index4.html', locals())



