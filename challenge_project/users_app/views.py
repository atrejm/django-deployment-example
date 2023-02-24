from django.shortcuts import render
from django.http import HttpResponse 
from users_app.models import UserModel

# Create your views here.
def users(request):
    context_dir = {
        "users_DB" : UserModel.objects.all()
    }

    return render(request, "challenge_project/users.html", context_dir)

def home(request):
    return(HttpResponse("Home page.."))