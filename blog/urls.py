from django.urls import path 
from .views import (
    ArticleView ,
    ArticleDetailView ,
    CreateArticle ,
    UpdateArticleView ,
    DeleteArticleView
)
app_name = 'articles'
urlpatterns=[
    path('' , ArticleView.as_view() , name='article-list'),
    path('<int:id>/' , ArticleDetailView.as_view() , name='article-detail') ,
    path('create/' , CreateArticle.as_view() , name='article-create') ,
    path('<int:id>/update/' , UpdateArticleView.as_view() , name='article-update') ,
    path('<int:id>/delete/' , DeleteArticleView.as_view() , name='article-delete') ,

]