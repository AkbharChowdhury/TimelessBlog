from django.contrib.auth.models import User
from django.contrib.auth.views import PasswordChangeView
from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView

from .forms import RegisterForm, EditProfileForm, EditPasswordForm, ProfilePageForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from articles.models import Profile  # this is not an error


class CreateProfilePage(CreateView):
    model = Profile
    template_name = 'registration/create_user_profile.html'
    form_class = ProfilePageForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class EditProfilePage(generic.UpdateView):
    model = Profile
    template_name = 'registration/edit_profile_page.html'
    fields = [
        'bio',
        'profile_pic',
        'twitter_url',
        'instagram_url',
        'pinterest_url'
    ]

    success_url = reverse_lazy('home')


class ShowProfilePage(DetailView):
    model = Profile
    template_name = 'registration/user_profile.html'

    def get_context_data(self, *args, **kwargs):
        context = super(self.__class__, self).get_context_data(*args, **kwargs)
        context['page_user'] = get_object_or_404(Profile, id=self.kwargs['pk'])

        return context


def password_success(request):
    return render(request, 'registration/password_success.html', {})


class ChangePasswordForm(PasswordChangeView):
    # form_class = PasswordChangeForm
    form_class = EditPasswordForm
    success_url = reverse_lazy('password_success')


class RegisterForm(generic.CreateView):
    form_class = RegisterForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')


class ProfileForm(generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user
