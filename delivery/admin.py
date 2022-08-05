from django.contrib import admin
from .models import Produto, Restaurante, Pedido, ItemPedido
from .forms import RestauranteForm, ProdutoForm, PedidoForm, ItemPedidoForm
# Register your models here.

class ProdutoAdminStackedInline(admin.StackedInline):
    model = Produto
    form = ProdutoForm
class RestauranteAdmin(admin.ModelAdmin):
    model = Restaurante
    form = RestauranteForm
    inlines = [ProdutoAdminStackedInline]

class ItemPedidoAdminStackedInline(admin.ModelAdmin):
     model = ItemPedido
     form = ItemPedidoForm
     readonly_fields=('valor_total',)
class PedidoAdmin(admin.ModelAdmin):
     model = Pedido
     form = PedidoForm
     readonly_fields=('valor_total',)



admin.site.register(Restaurante, RestauranteAdmin)
admin.site.register(Pedido, PedidoAdmin)
