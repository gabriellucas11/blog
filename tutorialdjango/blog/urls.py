from django.urls import path

from . import views 
#variavel para conseguir referenciar as urls do arquivo
app_name = "blog"
#lista de padroes de url   
urlpatterns =[
    #quando passar urls sem passar argumentos cairemos na lista de posts
    path("", views.PostListView.as_view(), name="list"),
    #quando acessarmos uma url passando o slug de um post como argumento ai acessamos a pagina desse post
    path("<slug:slug>/", views.PostDetailView.as_view(), name="detail"),
]