from django import forms
from .models import Article, Category, Comment

choices = Category.objects.all().values_list('name', 'name')
choice_list = [item for item in choices]


class CreateArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title',
                  'title_tag',
                  'author',
                  'category',
                  'body',
                  'snippet',
                  'image'
                  )
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'title',
                'autofocus': 'true'
            }),
            'title_tag': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'enter the blog title.This will display on the title tag of the web browser'

            }),
            'author': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'author',
                'type': 'hidden',
            }),
            'category': forms.Select(
                choices=choice_list,
                attrs={
                    'class': 'form-select'
                }),
            'body': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'enter body'

            }),
            'snippet': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'enter body'

            }),

        }


class EditArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title', 'title_tag', 'category', 'body', 'snippet', 'image')
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'title...'
            }),
            'title_tag': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'enter the blog title.This will display on the title tag of the web browser'

            }),
            'category': forms.Select(
                choices=choice_list,
                attrs={
                    'class': 'form-control'
                }),
            'author': forms.Select(attrs={
                'class': 'form-control'
            }),
            'body': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'enter body'

            }),
            'snippet': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'enter body'

            }),

        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('article',
                  'name',
                  'body'
                  )
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'autofocus': 'true',

            }),

            'body': forms.Textarea(attrs={
                'class': 'form-control',

            }),

        }


class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'body')
        # widgets = {
        #     'name': forms.TextInput(attrs={
        #         'class': 'form-control',
        #         'autofocus': 'true',
        #
        #     }),
        #
        #     'body': forms.Textarea(attrs={
        #         'class': 'form-control',
        #
        #     }),
        #
        # }
