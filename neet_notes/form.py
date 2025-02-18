from django import forms

class logForm(forms.Form):
    name = forms.CharField(max_length=10, required=True, widget=forms.TextInput(attrs={
        'placeholder': 'Your name',
        "autocomplete": "off"
    }))
    
    password = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Password',
        "autocomplete": "off"
    }))
    
    
