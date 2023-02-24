from django.shortcuts import render
from . import forms
from . models import PersonModel
# Create your views here.

def index(request):
    return render(request, 'basicapp/index.html')

def form_name_view(request):
    form = forms.FormName()

    if request.method == 'POST':
        form = forms.FormName(request.POST)

        if form.is_valid():
            #Do something
            profile = form.save()
            profile.user = request.user
            profile.save()
            print("VALIDATION SUCESS!")
            print("Name: " + form.cleaned_data['name'])

    return render(request,'basicapp/form_page.html',{'form':form})

def show_users(request):
    user_data = {'user_data_DB': PersonModel.objects.all()}
        
    return render(request, 'basicapp/user_page.html',user_data)