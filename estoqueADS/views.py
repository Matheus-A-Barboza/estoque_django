from django.shortcuts import render, redirect
from .models import Produtos, Categoria
from datetime import datetime

def index(request):
    produtos = Produtos.objects.all()
    return render(request, 'pages/index.html', {'produtos': produtos})

def adicionar_produto(request):
    
    if request.method == "POST":
        nome = request.POST['nome']
        categoria = request.POST['categoria']
        preco = request.POST['preco']
        descricao = request.POST['descricao']
        quantidade = request.POST['quantidade']
        codigo = request.POST['codigo']
        em_estoque = False
        
        if int (quantidade) > 0:
            em_estoque = True
        data_criacao = datetime.now()
        
        Produtos.objects.create(
            nome=nome,
            categoria_id=categoria,
            preco=preco,
            descricao=descricao,
            quantidade=quantidade,
            em_estoque=em_estoque,
            codigo=codigo,
            data_criacao=data_criacao
        )
        
        return redirect('index')
        
    else:
        categorias = Categoria.objects.all()
        return render(request, 'pages/adicionar_produto.html', {'categorias': categorias})
    
def produto(request, id):
    detalhe = Produtos.objects.get(id=id)
    return render(request, 'pages/produto.html', {'detalhe':detalhe})

def excluir(request, id):
    produto = Produtos.objects.get(id=id).delete()
    return redirect('index')