from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class HomeView(View):
    def get(self, request):
        context = {
            'title': 'main page',
        }
        if request.user.is_authenticated:
            context['user_name'] = request.user.username
        return render(request, 'main.html', context=context)

    def post(self, request):
        context = {
            'title': 'POST'
        }
        return render(request, "main.html", context=context)

class RegisterView(View):
    def get(self, request):
        form = UserCreationForm()
        return render(request, 'signup.html', {'form': form})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('main')
        return render(request, 'signup.html', {'form': form})

class LoginView(View):
    def get(self, request):
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})

    def post(self, request):
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('main')
        return render(request, 'login.html', {'form': form})

from django.contrib.auth import logout
from django.utils.decorators import method_decorator
from django.views.decorators.http import require_POST

class LogoutView(View):
    @method_decorator(require_POST)
    def post(self, request):
        logout(request)
        return redirect('login')

