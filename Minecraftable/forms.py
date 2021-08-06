from django import forms


class NewDatapackForm(forms.Form):
    location = forms.CharField(label='Location', max_length=200, widget=forms.TextInput(attrs={'id': 'location-field'}))
    name = forms.CharField(label='Name', max_length=200, widget=forms.TextInput(attrs={'id': 'name-field'}))