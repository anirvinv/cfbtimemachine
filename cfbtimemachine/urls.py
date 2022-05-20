from django.urls import path, re_path
from django.conf.urls import url
from cfbtimemachine.models import Article
from .views import ArticleListView, otherUrls
from . import views

urlpatterns = [
    path('', ArticleListView.as_view(), name='home'),
    path('iframe/<int:id>', views.iframe, name='iframe'),
    re_path(r'/.*/', views.otherUrls)
]
