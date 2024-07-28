from django.urls import reverse_lazy
from django.shortcuts import redirect, render
from django.views.generic import TemplateView, FormView, View
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required
from .forms import *

# Create your views here.

class IndexView(View):
    template_name = "pages/index.html"
    
    @login_required
    def get(self, request):
        return render(request, self.template_name, context={})

class SignInView(View):
    form_class = LoginForm
    template_name = 'registration/signin.html'

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, context={'form': form})

    def post(self,request):
        form = self.form_class(data=request.POST)

        if form.is_valid():
            user = self.form_class.get_user()
            login(request, user)
            return redirect("index")
        return render(request, self.template_name, context={"forms":form})

    
class RegisterView(View):
    template_name = "registration/signup.html"
    form_class = RegisterForm
    
    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, context={'form':form})
    
    def post(self,request):
        form = self.form_class(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect("signin")
        return render(request, self.template_name, context={'form':form})