from django import forms

class FormularioContacto(forms.Form):
    
    asunto = forms.CharField(max_length=30, label="Asunto", widget=forms.TextInput(
        attrs={'class': "form-control"}))

    contenido = forms.CharField(max_length=300, label="Contenido", widget=forms.Textarea(
        attrs={'class': "form-control"}))
    
    
    
    
    
    
    
    