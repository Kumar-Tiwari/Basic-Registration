from django import forms
from django.contrib.auth.models import User

class Signup_Form(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput(attrs={
        "autocomplete":"new-password",
    }))
    class Meta:
        model=User
        fields=["username","first_name","last_name","email","password"]
    
    def clean_username(self):
        username=self.cleaned_data['username']
        try:
            user=User.objects.get(username=username)
            raise forms.ValidationError("Username already exists")
        except:
            pass