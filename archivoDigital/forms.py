from django import forms
from django.contrib.auth import forms as auth_forms
from archivoDigital.models import User

class UserCreationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email','first_name','last_name')

    def gen_passwd(length=8):
        chars = string.letters + string.digits
        return ''.join([choice(chars) for i in range(length)])

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        passW=User.objects.make_random_password()
        print(passW)
        user.set_password(passW)
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    password = auth_forms.ReadOnlyPasswordHashField(label="Password",
        help_text="Raw passwords are not stored, so there is no way to see "
                  "this user's password, but you can change the password "
                  "using <a href=\"password/\">this form</a>.")

    class Meta:
        model = User
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(UserChangeForm, self).__init__(*args, **kwargs)
        f = self.fields.get('user_permissions', None)
        if f is not None:
            f.queryset = f.queryset.select_related('content_type')

    def clean_password(self):
        return self.initial["password"]
