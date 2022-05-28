from django.urls import path, re_path
from .views import ArticleListView, FilterListView
from . import views

urlpatterns = [
    path('', ArticleListView.as_view(), name='home'),
    path('filter/<str:college_id>/<str:player_id>', FilterListView.as_view(), name='filter'),
    path('iframe/<int:id>', views.iframe, name='iframe'),
    re_path(r'/.*/', views.otherUrls)
]
