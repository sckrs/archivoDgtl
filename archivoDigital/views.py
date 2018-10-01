from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def changePass(request):
    var = request.POST['name']
    return HttpResponse("<em>My Second Project</em> {}".format(var))
