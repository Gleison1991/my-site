from django.urls import path
from mysite.blog.views.post_view import PostView

urlpatterns = [
    path('', PostView.as_view(), name='home')
]
