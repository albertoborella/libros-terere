from django.forms import ModelForm, Textarea
from .models import Contacto

class ContactoForm(ModelForm):

    class Meta:
        model = Contacto
        fields = '__all__'
        widgets = {
            'texto': Textarea(attrs={'cols': 80, 'rows': 2}),
        }
        
