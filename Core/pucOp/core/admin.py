from django.contrib import admin
from .models import Oportunidade, Tag, Contato


class TagInline(admin.TabularInline):
    model = Tag
    extra = 1


class ContatoInline(admin.TabularInline):
    model = Contato
    extra = 1


@admin.register(Oportunidade)
class OportunidadeAdmin(admin.ModelAdmin):
    list_display = ("nome", "categoria", "resumo")
    list_filter = ("categoria",)
    search_fields = ("nome", "descricao")
    inlines = [TagInline, ContatoInline]


admin.site.register(Tag)
admin.site.register(Contato)
