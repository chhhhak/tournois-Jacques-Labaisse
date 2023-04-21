from django.forms import ModelForm
from .models import Commentaire

class CommentForm(ModelForm):
    class Meta:
        model = Commentaire
        # fields = ['author', 'match', 'date', 'text']
        fields = ['text']