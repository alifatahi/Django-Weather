from django.forms import ModelForm, TextInput
from .models import City


# Model Form is for Create Form Class From our Model
class CityForm(ModelForm):
    class Meta:
        # Declare Model
        model = City
        # Declare Field
        fields = ['name']
        # we specify Custom widget for field
        # For example here we declare placeholder and class
        widgets = {
            'name': TextInput(attrs={'class': 'input', 'placeholder': 'City Name'}),
        }  # updates the input class to have the correct Bulma class and placeholder
