from .models import MessageModel
from django.forms import ModelForm


class MassegeModelForm(forms.ModelForm):

    class Meta: 
        model = MessageModel
        exclude = ['created_at']
        