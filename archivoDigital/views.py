from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.
def userLogin(request):
        if request.method == 'POST':
            # First get the username and password supplied
            email = request.POST.get('email')
            password = request.POST.get('password')
            # Django's built-in authentication function:
            user = authenticate(email=email, password=password)
            # If we have a user
            if user:
                login(request,user)
                return archivoDigital(request,email)
            else:
                return render(request, 'login_templates/login.html', { 'error':True,'mensaje':"El correo/contraseña son incorrectos" })

        else:
            #Nothing has been provided for username or password.
            return render(request, 'login_templates/login.html', {})

@login_required
def user_logout(request):
    # Log out the user.
    logout(request)
    # Return to homepage.
    return HttpResponseRedirect(reverse('userLogin'))

@login_required
def archivoDigital(request,email):
    return HttpResponse("accediste {0}".format(email))
