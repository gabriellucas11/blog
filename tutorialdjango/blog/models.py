from django.db import models
from django.forms import SlugField
from django.contrib.auth.models import User
from django.urls import reverse
#permite criar tabelas no banco de dados sem escrever no sql
#armazenar posts
class Post(models.Model):
    #CharField indica que esse campo tem que receber Strings de até (no caso)255 caracteres 
    title = models.CharField(max_length=255)
    #para definir o texto que vamos usar na url(/introducao-ao-django)
    slug = models.SlugField(max_length=255, unique=True)
    #vai guardar o ID do autor do post  
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    #body e o texto do corpo(TextField e ideal para o corpo de um post pois não estamos preocupados com o número de caracteres )
    body = models.TextField()
    #vai adicionar automaticamente a data e a hora que o arquivo foi criado
    created = models.DateTimeField(auto_now_add=True)
    #update informa data e hora da ultima atualização
    update = models.DateTimeField(auto_now=True)
    #para deixar a descrição do post de acordo com o title

    #para mudar a ordem do das postagens deixando a mais recente primeiro 
    class Meta:
        ordering = ("-created",)

    def __str__(self): 
        return self.title
    #definir a url de um post
    def get_absolute_url(self):
        return reverse("blog:detail",kwargs={"slug": self.slug})