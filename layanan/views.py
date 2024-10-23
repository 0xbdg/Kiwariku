from django.shortcuts import redirect, render
from django.views.generic import View
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from .forms import LoginForm

# Create your views here.
class SignInView(View):
    form_class = LoginForm
    template_name = 'pages/signin.html'

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, context={'form': form})

    def post(self,request):
        form = self.form_class(data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("profile")
        return render(request, self.template_name, context={"form":form})

@login_required
def ChangePasswordPage(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, 'pages/change_password.html', context={'form':form})

@login_required
def signout(request):
    logout(request)
    return redirect("signin")

@login_required
def ProfilePage(request):
    return render(request, "pages/profile.html", context={})