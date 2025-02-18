from django import forms

class msgForm(forms.Form):
    message = forms.CharField(max_length=300, required=True, widget=forms.TextInput(attrs={
        'placeholder': "Type here...",
        "autocomplete": "off"
    }))