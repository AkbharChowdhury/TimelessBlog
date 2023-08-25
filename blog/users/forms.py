from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from django import forms
from articles.models import Profile  # this is not an error
# from blog.articles.models import Profile


class ProfilePageForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = (
            'bio',
            'profile_pic',
            'facebook_url',
            'twitter_url',
            'instagram_url',
            'pinterest_url'

        )

        widgets = {

            'bio': forms.Textarea(attrs={
                'class': 'form-control',
                'autofocus': 'true',

            }),


            'facebook_url': forms.TextInput(attrs={
                'class': 'form-control',

            }),
            'twitter_url': forms.TextInput(attrs={
                'class': 'form-control',

            }),
            'instagram_url': forms.TextInput(attrs={
                'class': 'form-control',

            }),
            'pinterest_url': forms.TextInput(attrs={
                'class': 'form-control',

            }),

        }


class EditPasswordForm(PasswordChangeForm):
    context = {'class': 'form-control',
               'type': 'password',
               }
    old_password = forms.CharField(max_length=100, widget=forms.PasswordInput(context))
    new_password1 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs=context))
    new_password2 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs=context))

    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')


class RegisterForm(UserCreationForm):
    # first_name = forms.CharField(max_length=2, widget=forms.TextInput(attrs={'class': 'form-control'}))
    # last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    # email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    # username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    # password1 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    # password2 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={
    #     'class': 'form-control',
    #     'label': 'Confirm password'
    # }))
    PASSWORD_MAX_LENGTH = 30
    first_name = forms.CharField(max_length=100, widget=forms.TextInput())
    last_name = forms.CharField(max_length=100, widget=forms.TextInput())
    email = forms.EmailField(widget=forms.EmailInput())
    username = forms.CharField(max_length=100, widget=forms.TextInput())
    password1 = forms.CharField(max_length=PASSWORD_MAX_LENGTH, widget=forms.PasswordInput())
    password2 = forms.CharField(max_length=PASSWORD_MAX_LENGTH, widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
        help_texts = {'username': "Unique identifier for the username", }

    def __int__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        # self.fields['email'].label = 'EMAIL FOR'
        # error_css_class = "error"

        # self.fields['username'].widget.attrs['class'] = "form-control"
        # self.fields['username'].widget.attrs['class'] = 'form-control'
        # self.fields['password1'].widget.attrs['class'] = 'form-control'
        # self.fields['password2'].widget.attrs['class'] = 'form-control'


class EditProfileForm(UserChangeForm):
    username = forms.CharField(max_length=2, widget=forms.TextInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=2, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=2, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password = forms.PasswordInput()

    last_login = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    date_joined = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username',
                  'first_name',
                  'last_name',
                  'email',
                  'password',
                  'last_login',
                  'date_joined'
                  )
