from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import extras
from django.contrib.auth.models import User

class RegisterForm(forms.ModelForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')

    ADMIN = 'Admin'
    STUDENT = 'Student'
    TOURIST = 'Tourist'
    BUSINESSMAN = 'Businessman'

    ACCOUNTTYPE = (
        (ADMIN, 'Admin'),
        (STUDENT, 'Student'),
        (TOURIST, 'Tourist'),
        (BUSINESSMAN, 'Businessman')
    )

    accountType = forms.ChoiceField(widget=forms.Select(), choices=ACCOUNTTYPE, initial="", label="User type", required=True)
    # birthDate = forms.DataField(widget=extras.SelectDateWidget)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'accountType')
