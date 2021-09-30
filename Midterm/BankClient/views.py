from django.shortcuts import render,redirect
from django.views.generic import View
from .forms import *
# Create your views here.


class IndexView(View):
    def get(self,request):
        client = Client.objects.all()
        return render(request,'index.html',{'clients':client})
    def post(self,request):
        form = ClientForm(request.POST)
        if form.is_valid():
            name = request.POST.get("name")
            address = request.POST.get("address")
            birthdate = request.POST.get("birthdate")
            mobile_number = request.POST.get("mobile_number")
            form = Client(name=name,address=address,birthdate=birthdate,mobile_number=mobile_number)
            form.save()
            return redirect('./index')

