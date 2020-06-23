from django.forms import ModelForm
from .models import TeachingContent

class TeachingContentForm(ModelForm):
    class Meta:
        model = TeachingContent
        fields = "__all__"