from django.shortcuts import render,redirect
from  django.contrib.auth.views import LoginView
from  django.contrib.auth import logout
from django.views.generic import CreateView
from .forms import RegisterForm

# Create your views here.

class RegisterView(CreateView):
    template_name = "register.html"
    form_class = RegisterForm
    success_url = "/"

class MyLoginView(LoginView):
    template_name = "login.html"
    # success_url = "/"
    # redirect_authenticated_user = True

    def get_success_url(self) -> str:
        return self.request.GET.get("next","/")
        # return "/"


def logout_view(request):
    logout(request)
    return redirect("main:index")