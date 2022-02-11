from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    #para customisar a interface 
    list_display = ("title", "slug", "author", "created", "update")
    #para qundo eu escrever o titulo ja ir para o slug diretamente sem precisar ser prenchido de forma manual
    prepopulated_fields = {"slug": ("title",)}

