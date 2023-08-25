from django.urls import path

from . import views

urlpatterns = [
    path('', views.ArticleList.as_view(), name='home'),
    path('article/<int:pk>', views.ArticleDetails.as_view(), name='article_detail'),
    path('create_post/', views.CreateArticle.as_view(), name='create_article'),
    path('article/edit/<int:pk>', views.EditArticle.as_view(), name='edit_article'),
    path('article/<int:pk>/remove', views.DeleteArticle.as_view(), name='delete_article'),
    path('create_category/', views.CreateCategory.as_view(), name='create_category'),
    path('category/<str:cats>/', views.CategoryList, name='category'),
    path('category-list/', views.CategoryListView, name='category_list'),
    path('comment/<int:pk>/comment/', views.CreateComment.as_view(), name='create_comment'),

]
