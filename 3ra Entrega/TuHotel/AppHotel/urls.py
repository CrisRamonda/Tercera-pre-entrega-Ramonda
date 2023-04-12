from django.urls import path
from AppHotel.views import *

urlpatterns = [
    path('', inicio, name='Inicio'),
    path('registo-cliente/', registro_cliente, name = 'RegistroClientes'),
    path('lista-clientes/', lista_clientes, name = 'ListaClientes'),
    path('cliente-buscado/', cliente_buscado, name = 'ClienteBuscado'),
    path('registro-reserva/', registro_reserva, name = 'RegistroReservas'),
    path('ver-reservas/', ver_reservas, name = 'VerReservas'),
]
