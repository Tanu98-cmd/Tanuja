from django.forms import ModelForm
from .models import *
class Fileform(ModelForm):
    class Meta:
        model=Files
        fields='__all__'
