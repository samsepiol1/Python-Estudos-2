from django.shortcuts import render,HttpResponse

# Create your views here.

def pagina_inicial(request):
    return HttpResponse("Bem Vindo a página do APPS de contas")



