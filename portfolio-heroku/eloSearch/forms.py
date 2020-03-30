from django import forms


class SummonerForm(forms.Form):
    name = forms.CharField(max_length=120)
