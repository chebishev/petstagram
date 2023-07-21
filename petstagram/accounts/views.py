from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from petstagram.accounts.forms import RegisterUserForm


class RegisterUserView(CreateView):
    template_name = 'register-page.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        result = super().form_valid(form)

        login(self.request, self.object)

        return result

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['next'] = self.request.GET.get("next", '')

        return context

    def get_success_url(self):
        return self.request.POST.get("next", self.success_url)


class LoginUserView(LoginView):
    template_name = 'login-page.html'
    success_url = 'index'


class LogoutUserView(LogoutView):
    pass


def profile_details(request, pk):
    return render(request, 'profile-details-page.html')


def profile_edit(request, pk):
    return render(request, 'profile-edit-page.html')


def profile_delete(request, pk):
    return render(request, 'profile-delete-page.html')
