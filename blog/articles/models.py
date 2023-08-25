from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils.html import mark_safe
from ckeditor.fields import RichTextField


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField()
    profile_pic = models.ImageField(null=True, blank=True, upload_to='images/profile/')
    facebook_url = models.URLField(null=True, blank=True)
    twitter_url = models.URLField(null=True, blank=True)
    instagram_url = models.URLField(null=True, blank=True)
    pinterest_url = models.URLField(null=True, blank=True)

    def __str__(self):
        return str(self.user)

    def get_absolute_url(self):
        return reverse('home')


class Category(models.Model):
    name = models.CharField(max_length=100)
    css_class = models.CharField(max_length=100, blank=True)
    path_d = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home')


class Article(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(null=True, blank=True, upload_to='images/')
    title_tag = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = RichTextField(blank=True, null=True)
    publication_date = models.DateField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_query_name='category_id')
    snippet = models.CharField(max_length=100)
    likes = models.ManyToManyField(User, related_name='article_likes', blank=True)

    class Meta:
        ordering = ['-publication_date']

    def total_records(self):
        return self.title.count()

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return f'{self.title} | {self.author}'

    def get_snippet(self):
        return mark_safe(f'{self.body[:200]}...')

    def get_absolute_url(self):
        # return reverse('article_detail', args=str(self.id))
        return reverse('home')


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments', blank=False, null=False)
    name = models.CharField(max_length=255, blank=False, null=False)
    body = models.TextField(blank=False, null=False)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.article.title} | {self.name}'
