from django import forms

class RegistroCliente(forms.Form):

    nombre = forms.CharField(max_length=100)
    documento = forms.IntegerField()
    email = forms.EmailField(max_length=300)