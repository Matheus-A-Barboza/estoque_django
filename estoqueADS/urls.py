from django.urls import path, include
from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('adicionar_produto/', views.adicionar_produto, name='adicionar_produto')
]