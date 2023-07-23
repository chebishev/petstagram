from django.contrib.auth import login, get_user_model
from django.contrib.auth.views import LoginView, LogoutView
from django.templatetags.static import static
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from petstagram.accounts.forms import RegisterUserForm, LoginUserForm

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
    form_class = LoginUserForm

class LogoutUserView(LogoutView):
    next_page = reverse_lazy("login")


class ProfileDetailsView(DetailView):
    template_name = 'profile-details-page.html'
    model = UserModel

    profile_image = static('images/person.png')

    def get_profile_picture(self):
        if self.object.profile_picture is not None:
            return self.object.profile_picture
        return self.profile_image

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['profile_image'] = self.get_profile_picture()
        context['pets'] = self.request.user.pet_set.all()

        return context

class ProfileEditView(UpdateView):
    template_name = 'profile-edit-page.html'

class ProfileDeleteView(DeleteView):
    template_name = 'profile-delete-page.html'