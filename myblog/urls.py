from django.urls import path
from .views import blog_view, single_blog_view,test,blog_category,blog_search,newspaper

app_name = 'myblog'

urlpatterns = [
    path('', blog_view, name='blog_home'),
    path('myblog/<int:pid>/', single_blog_view, name='blog_single'),
    path('category/<str:cat_name>/', blog_view, name='category'),
    path('tag/<str:tag_name>/', blog_view, name='tag'),
    path('author/<str:author_username>/', blog_view, name='author'),
    path('search/', blog_search, name='search'),
    path('test/', test, name="test"),
    path('newspaper/', newspaper, name='newspaper'),
]