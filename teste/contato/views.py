from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.core.paginator import Paginator
from .forms import UsuarioForm
from .models import Usuario

# Create your views here.
from django.shortcuts import render_to_response
from .forms import *

def cadastrar_usuario(request):
    form = UsuarioForm()
    if (request.method == 'POST'):
        form = UsuarioForm(request.POST)
        if (form.is_valid()):
            post_name = form.cleaned_data['nome']
            post_email = form.cleaned_data['email']
            post_sexo = form.cleaned_data['sexo']
            new_post = Usuario(nome=post_name, sexo=post_sexo, email=post_email)
            new_post.save()
            return HttpResponse('Cadastro realizado com Sucesso')
    elif (request.method == 'GET'):
        return render(request, "contato.html", {'form': form})

