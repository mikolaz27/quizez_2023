from django.urls import include, path

from blog.views import create_blog, all_blogs

urlpatterns = [
    path("create/", create_blog, name='create_blog'),
    path("", all_blogs, name='all_blogs'),
]
