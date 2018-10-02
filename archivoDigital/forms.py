from django import forms
from django.contrib.auth import forms as auth_forms
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
from archivoDigital.models import User

class UserCreationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email','first_name','last_name')

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        form = self.cleaned_data
        passW=User.objects.make_random_password()
        user.set_password(passW)
        sender(passW,form['email'],'Bienvenido al Archivo Digital','Su usuario ha sido creado exitosamente.')
        if commit:
            user.save()
        return user

class UserChangeForm(forms.ModelForm):

    password = auth_forms.ReadOnlyPasswordHashField(label="Contraseña",#)
        help_text="Puede cambiar la contraseña activando este checkbox"
                  "&nbsp;&nbsp;&nbsp;<input id=\"one\" type=\"checkbox\" value=\"Cambiar Contraseña\" name=\"changePass\">")

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

    def save(self,commit=True):
        data=self.cleaned_data
        user = super(UserChangeForm, self).save(commit=False)
        if data['changePass']=='change':
            data['changePass']==''
            passW=User.objects.make_random_password()
            sender(passW,data['email'],'Su clave de acceso al Archivo Digital ha sido modificada','Su usuario ha sido creado exitosamente.')
            user.set_password(passW)
        if commit:
            user.save()
        return user

def sender(passW,to,subject,message):
    from_email=settings.EMAIL_HOST_USER
    to_email=[to]
    extraMessage = 'Sus claves de acceso son usuario: {0}, Contraseña: {1}'.format(to,passW)
    send_mail(subject=subject,from_email=from_email,recipient_list=to_email,message=message.join([extraMessage]))
    
