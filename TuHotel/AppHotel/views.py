from django.shortcuts import render
from .models import Cliente
from django.http import HttpResponse
from .forms import RegistroCliente

def inicio(self):

    return render(self, 'inicio.html')


def registro_cliente(self):
           
    if self.method == 'POST':
        
        miFormulario = RegistroCliente(self.POST)

        print(miFormulario)

        if miFormulario.is_valid():

            data = miFormulario.cleaned_data
        
            cliente = Cliente(
                nombre = data['nombre'],
                documento = data['documento'], 
                email = data['email'],              
            )
            cliente.save()
    
        return render(self,'inicio.html')
    
    else:
        
        miFormulario = RegistroCliente()

        return render(self, 'registro_cliente.html', {'miFormulario ' : miFormulario})
 
   
def lista_clientes(self):

    clientes = Cliente.objects.all()

    return render(self, 'lista_clientes.html', {'lista_clientes':clientes})


def registro_reserva(self):

    return render(self, 'registro_reserva.html')


def ver_reservas(self):

    return render(self, 'ver_reservas.html')