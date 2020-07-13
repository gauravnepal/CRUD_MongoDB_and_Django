from django import forms
from .models import Movies


# DataFlair
class MovieCreate(forms.ModelForm):
    class Meta:
        model = Movies
        fields = '__all__'
