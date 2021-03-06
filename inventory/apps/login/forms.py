#
# login/forms.py
#

import re
import logging

from django import forms
from django.contrib.auth import get_user_model

log = logging.getLogger('inventory.apps.login.forms')
User = get_user_model()


class LoginForm(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(widget=forms.PasswordInput(render_value=False),
                               max_length=30)


class RegistrationForm(forms.Form):
    username = forms.CharField(label=u'Username',
                               max_length=30)
    email = forms.EmailField(label=u'E-mail address')
    password1 = forms.CharField(widget=forms.PasswordInput(render_value=False),
                                label=u'Password',
                                max_length=128)
    password2 = forms.CharField(widget=forms.PasswordInput(render_value=False),
                                label=u'Password (again)',
                                max_length=128)

    def clean_username(self):
        reValidUser = re.compile(r"^(\w+)$")

        if not reValidUser.search(self.cleaned_data['username']):
            msg = u'Usernames can only contain letters, ' + \
                  u'numbers and underscores.'
            log.info(msg)
            raise forms.ValidationError(msg)

        try:
            user = User.objects.get(username=self.cleaned_data['username'])
        except User.DoesNotExist:
            return self.cleaned_data['username']

        msg = u'This username is already taken. Please choose another.'
        log.info(msg)
        raise forms.ValidationError(msg)

    def clean_password2(self):
        if self.cleaned_data['password1'] != self.cleaned_data['password2']:
            msg = u'You must type the same password both times.'
            log.info(msg)
            raise forms.ValidationError(msg)

        return self.cleaned_data['password2']

    def save(self):
        data = self.cleaned_data
        log.debug("cleaned_data: %s", data)
        return User.objects.create_user(username=data['username'],
                                        email=data['email'],
                                        password=data['password1'])
