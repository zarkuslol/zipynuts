from django.contrib import admin
from zipynuts.models import Produto

class Produtos(admin.ModelAdmin):

    list_display = (
        'id', 
        'nome', 
        'preço', 
        'quantidade',
        'peso_em_gramas', 
        'data_de_fabricação', 
        'data_de_validade',
    )
    list_display_links = (
        'id', 
        'nome', 
        'preço', 
        'quantidade',
        'peso_em_gramas', 
        'data_de_fabricação', 
        'data_de_validade',
    )
    search_fields = (
        'id', 
        'nome', 
        'preço', 
        'quantidade',
        'peso_em_gramas', 
        'data_de_fabricação', 
        'data_de_validade',
    )

admin.site.register(Produto, Produtos)
