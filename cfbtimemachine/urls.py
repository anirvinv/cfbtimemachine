from django.urls import path, re_path
from .views import ArticleListView
from . import views

urlpatterns = [
    path('', ArticleListView.as_view(), name='home'),
    path('iframe/<int:id>', views.iframe, name='iframe'),
    re_path(r'/.*/', views.otherUrls)
]
