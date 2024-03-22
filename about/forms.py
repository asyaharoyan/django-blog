from django import forms
from .models import CollaborateRequest

class CollaborateForm(forms.ModelForm):
    """
    Form class for the users to send collaborations requests
    """
    class Meta:
        """
        Specify the django model and order of the fields
        """
        model = CollaborateRequest
        fields = ('name', 'email', 'message')
