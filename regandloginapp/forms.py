from django import forms
from .models import Reg,score
class RegForm(forms.ModelForm):
    class Meta:    
        model = Reg
        widgets = {'pwd': forms.PasswordInput(),}
        fields = ['user', 'pwd','email']
class LoginForm(forms.Form):
    user = forms.CharField(max_length=20)
    pwd = forms.CharField(widget=forms.PasswordInput())

class ScoreForm(forms.ModelForm):
    class Meta:
        model = score
        fields = ['first_round','second_round','third_round']

