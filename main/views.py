from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView
from django.contrib.auth.views import LoginView
from .forms import *

# Create your views here.

class IndexView(TemplateView):
    template_name = "pages/index.html"
    
    def get(self, request):
        pass

class SignInView(LoginView):
    form_class = LoginForm
    template_name = 'registration/signin.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        return super().form_valid(form)

    
class RegisterView(FormView):
    template_name = "registration/signup.html"
    form_class = RegisterForm
    success_url = reverse_lazy('signin')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)