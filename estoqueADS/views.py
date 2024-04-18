from django.shortcuts import render, HttpResponse


def index(request):
    frutas = ['Maçã', 'Uva', 'Jambo']
    return render(request, 'pages/teste.html', {"frutas": frutas})