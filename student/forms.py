# coding utf - 8
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.forms import AuthenticationForm
from django import forms
from django.forms import ModelForm
from student.models import *


class GroupForm(ModelForm):
	class Meta:
		model = Group

class StudForm(ModelForm):
	class Meta:
		model = Stud
		

class RegForm(forms.Form):
    email = forms.EmailField(widget=forms.TextInput(attrs={'maxlength':75}), label=_('Email'))
    password = forms.CharField(widget=forms.PasswordInput(render_value=False), label=_('Password'))

    def clean_email(self):
        if User.objects.filter(email__iexact=self.cleaned_data['email']):
            raise forms.ValidationError(_('This email address is already in use. Please supply a different email address.'))
        return self.cleaned_data['email']

    def save(self, request):
        login = uuid.uuid4().hex[:30]
        email = self.cleaned_data['email']
        password = self.cleaned_data['password']
        user = User.objects.create_user(login, email, password)

        return user

class LoginForm(AuthenticationForm):
    username = forms.CharField(label=_('login'), max_length=75)