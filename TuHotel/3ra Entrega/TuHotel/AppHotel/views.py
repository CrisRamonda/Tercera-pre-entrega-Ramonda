from django.shortcuts import render
from .models import Cliente
from django.http import HttpResponse

def inicio(self):

    return render(self, 'inicio.html')



def registro_cliente(self):
    
    if self.method == 'POST':
        cliente = Cliente(
            nombre = self.POST['nombre'],
            documento = self.POST['documento'],
            email = self.POST['email']
        )

        cliente.save()

        return render(self, 'inicio.html')
    

    return render(self,'registro_cliente.html')
    



def lista_clientes(self):

    # clientes = Cliente.objects.all()

    return render(self, 'lista_clientes.html')


def cliente_buscado(self):

    if self.GET['nombre']:

        nombre_consulta = self.GET['nombre']
        cliente = Cliente.objects.filter(nombre=nombre_consulta).first()

        return render(self, 'cliente_buscado.html', {"cliente":cliente})
    
    else: 
        return HttpResponse(f'No enviaste información')




def registro_reserva(self):

    return render(self, 'registro_reserva.html')

def ver_reservas(self):

    return render(self, 'ver_reservas.html')