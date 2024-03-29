from django.contrib import messages
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.http import HttpResponse
import json
from .forms import CreateArticleForm, EditArticleForm, CommentForm, CommentsForm
from .models import Article, Category, Comment

from django.http import JsonResponse
from dataclasses import dataclass

from django.shortcuts import redirect


@dataclass
class MyComment():
    article: Article
    name: str
    comment: str

    # def __iter__(self):
    #     return iter(astuple(self))

    def as_args(self):
        return (self.article, self.name, self.comment)

    def is_valid(self):
        return self.name and self.comment


def CategoryList(request, cats):
    category_slug = cats.replace('-', ' ')
    category_slug = Category.objects.filter(name=category_slug)

    category_name = [i.name for i in category_slug][0]
    category_id = [i.id for i in category_slug][0]
    category_blog = Article.objects.filter(category=category_id)

    context = {
        'category_name': category_name,
        'category_blog': category_blog,
    }
    return render(request, 'categories.html', context)


def CategoryListView(request):
    return render(request, 'category_menu_list.html', {'category_menu_list': Category.objects.all()})


class ArticleList(ListView):
    model = Article
    template_name = 'home.html'
    paginate_by = 6

    def get_queryset(self):

        search = {
            'title': self.request.GET.get('title'),
            'category': self.request.GET.get('category')
        }

        if search['title'] and search['category']:
            return self.search_filter(title=search['title'], category=search['category'])

        if search['category']:
            return self.search_filter(category=search['category'])

        if search['title']:
            return self.search_filter(title=search['title'])

        return Article.objects.all()

    def search_filter(self, title=None, category=None):
        article_filter = self.model.objects.filter

        if title and category is not None:
            return article_filter(

                Q(category_id=category) &
                Q(snippet__icontains=title)
            )

        if title:
            return article_filter(
                Q(title__icontains=title) |
                Q(body__icontains=title)
            )

        if category:
            return article_filter(
                Q(category_id=category)
            )

    def get_context_data(self, *args, **kwargs):
        context = super(self.__class__, self).get_context_data(*args, **kwargs)
        context['category_menu'] = Category.objects.all()
        context['total_records'] = self.get_queryset().count
        return context


class ArticleDetails(DetailView):
    id = 'article'
    model = Article
    template_name = 'article_detail.html'
    comment: Comment = None

    def toggle_like_article(self, article_id):
        article = get_object_or_404(self.model, id=article_id)
        article.likes.remove(self.request.user) if article.likes.filter(
            id=self.request.user.id).exists() else article.likes.add(
            self.request.user)
        return article_id

    def add_comment(self):
        article_id = self.request.POST.get(self.id)
        name = self.request.POST['name']
        body = self.request.POST['body']
        article = get_object_or_404(self.model, pk=article_id)
        print(type(article), 'is of type')
        comment = MyComment(article=article, name=name, comment=body)
        if not comment.is_valid():
            messages.error(self.request, 'please enter all the required fields')
            return article_id

        form = Comment(article=article, name=name, body=body)
        form.save()
        messages.success(self.request, 'your comment has been saved!')
        return article_id

    def is_ajax(self, request):
        return request.headers.get('x-requested-with') == 'XMLHttpRequest'

    def is_fetch_request(self, request):
        return request.headers.get('X-Csrftoken') is not None

    def like_data(self, context={}):
        article_likes = get_object_or_404(self.model, id=self.kwargs['pk'])
        liked = False if article_likes.likes.filter(id=self.request.user.id).exists() else True
        context['total_likes'] = article_likes.total_likes()
        context['liked_icon'] = 'fa-regular' if liked else 'fa-solid'
        context['liked'] = liked
        return context;

    def get_article_id_form_data(self):
        return json.loads(self.request.body.decode('utf-8'))[self.id]

    def handle_toggle_like(self):
        article_id = self.request.POST.get(self.__get_article_id()) or self.get_article_id_form_data()
        self.toggle_like_article(article_id)
        return JsonResponse(self.like_data())

    def post(self, request, *args, **kwargs):
        if self.is_ajax(request) or self.is_fetch_request(request):
            article_id = self.request.POST.get(self.id) or self.get_article_id_form_data()
            self.toggle_like_article(article_id)
            return JsonResponse(self.like_data())

        if 'btn_add_comment' in self.request.POST:
            # form = CommentForm()
            form = CommentForm(request.POST)
            print(self.request.POST, 'data')
            # print(form.is_valid())
            # if form.is_valid():
            #     print(form.cleaned_data)
            #     name = form.cleaned_data['name']
            context = {
                'form': form,
                'name': 'hello'
            }
            # name = form.cleaned_data['name']

            print('form')

            return HttpResponseRedirect(
                reverse(self.template_name.split('.')[0],
                        args=[
                            str(self.add_comment())
                        ]))

        if 'btn_toggle_like' in self.request.POST:
            like = self.like_article()
            return HttpResponseRedirect(reverse('article_detail', args=[str(like)]))

    def get_context_data(self, *args, **kwargs):
        context = super(self.__class__, self).get_context_data(*args, **kwargs)
        # article_likes = get_object_or_404(self.model, id=self.kwargs['pk'])
        article_likes = get_object_or_404(self.model, id=self.kwargs['pk'])
        print(self.args)

        liked = False if article_likes.likes.filter(id=self.request.user.id).exists() else True
        context['category_menu'] = Category.objects.all()
        self.like_data(context)
        article = get_object_or_404(self.model, pk=self.kwargs['pk'])
        context['author'] = f'{article.author.first_name} {article.author.last_name}'.title()
        post_data = self.request.body
        return context


class CreateArticle(CreateView):
    model = Article
    form_class = CreateArticleForm
    template_name = 'create_article.html'


class AddComment(CreateView):
    model = Comment
    form_class = CommentsForm
    template_name = 'article_detail.html'
    success_url = reverse_lazy('home')

    # success_url = reverse('article_detail', args=str(self.article_id))
    # def form_valid(self, form):
    #     form.instance.article_id = self.kwargs['pk']
    #     return super().form_valid(form)


class CreateComment(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'create_comment.html'
    # fields = '__all__'
    success_url = reverse_lazy('home')

    # success_url = reverse('article_detail', args=str(self.article_id))
    def form_valid(self, form):
        form.instance.article_id = self.kwargs['pk']
        return super().form_valid(form)


class EditArticle(UpdateView):
    model = Article
    form_class = EditArticleForm
    template_name = 'edit_article.html'

    def get_context_data(self, *args, **kwargs):
        context = super(self.__class__, self).get_context_data(*args, **kwargs)
        context['category_menu'] = Category.objects.all()
        return context


class DeleteArticle(DeleteView):
    model = Article
    template_name = 'delete_article.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *args, **kwargs):
        context = super(self.__class__, self).get_context_data(*args, **kwargs)
        context['category_menu'] = Category.objects.all()
        return context


class CreateCategory(CreateView):
    model = Category
    # form_class = CreateArticleForm
    template_name = 'create_category.html'
    fields = '__all__'

    def get_context_data(self, *args, **kwargs):
        context = super(self.__class__, self).get_context_data(*args, **kwargs)
        context['category_menu'] = self.model.objects.all()
        return context
