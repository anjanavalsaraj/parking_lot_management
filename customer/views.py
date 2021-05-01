from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import views as auth_views
from django.views import generic
from .forms import *
from django.contrib.auth import login
from django.contrib import messages
from .models import *
import datetime
# Create your views here.

class LoginView(auth_views.LoginView):
    template_name = 'user_login.html'

class UserSignUpView(generic.TemplateView):
    template_name = "signup.html"

    def get(self,request):
        form = UserRegistrationForm()
        return render(request, self.template_name, {"form":form})
    def post(self,request):
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("customer:home")
        form = UserRegistrationForm
        return render(request, self.template_name, {"form": form})


class HomePageView(generic.TemplateView):
    template_name = "home.html"


    def post(self,request):
        if 'entry-btn' in request.POST:

            vehicle_number = request.POST.get('reg-num')
            data = CustomerData.objects.create(customer=self.request.user, vehicle_number=vehicle_number,entry_time=datetime.datetime.now())
            return render(request, 'code.html',{"code": data.code})
        else:
            code = request.POST.get('code')
            try:
                data = CustomerData.objects.get(code=code)
                data.exit_time = datetime.datetime.now()
                data.save()
                return render(request, 'user_data.html', {"data": data})
            except:
                error_msg = "Invalid Code"
                return render(request,self.template_name,{"error":error_msg})


class LogoutView(auth_views.LogoutView):
    template_name = 'user_login.html'
