from django.contrib.auth import login, get_user_model
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from petstagram.accounts.forms import RegisterUserForm, LoginForm

UserModel = get_user_model()

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
    form_class = LoginForm

class LogoutUserView(LogoutView):
    next_page = reverse_lazy("login")


class ProfileDetailsView(DetailView):
    template_name = 'profile-details-page.html'
    model = UserModel


class ProfileEditView(UpdateView):
    template_name = 'profile-edit-page.html'

class ProfileDeleteView(DeleteView):
    template_name = 'profile-delete-page.html'