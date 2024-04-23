from django.shortcuts import render, HttpResponse
from .models import Produtos

def index(request):
    produtos = Produtos.objects.all()
    return render(request, 'pages/index.html', {'produtos': produtos})