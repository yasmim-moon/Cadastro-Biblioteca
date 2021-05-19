from django.db import forms
from .models import Livrob


class LivrosForm(forms.ModelForm):
    # titulo = forms.CharField(max_length=255)
    # autor= forms.CharField(max_length=255)
    # editora = forms.CharField(max_length=255)
    # categoria =  forms.CharField(max_length=255)

    class Meta:
        model = Livrob
        fields = '__all__'
