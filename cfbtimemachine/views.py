from django.shortcuts import redirect, render
from .models import Article,Conference, College, Player
from django.views.generic import ListView
import random
# Create your views here.


def home(request):
    context = {
        'articles': Article.objects.order_by('?')
    }
    return render(request, 'cfbtimemachine/home.html', context=context)


def otherUrls(request):
    return redirect('home')


class ArticleListView(ListView):
    model = Article
    template_name = 'cfbtimemachine/home.html'
    context_object_name = 'articles'
    # <app>/<model>_<viewtype>.html
    paginate_by = 10
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['conferences'] = Conference.objects.all()
        context['colleges'] = College.objects.all()
        context['players'] = Player.objects.all()
        return context
    
    def get_queryset(self):
        qs = super().get_queryset()
        ql = list(qs.exclude(img='nan').order_by('?')) + \
            list(qs.filter(img='nan'))
        return ql
    
class FilterListView(ListView):
    model = Article
    template_name = 'cfbtimemachine/home.html'
    context_object_name = 'articles'
    # <app>/<model>_<viewtype>.html
    paginate_by = 10
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['conferences'] = Conference.objects.all()
        context['colleges'] = College.objects.all()
        context['players'] = Player.objects.all()
        return context
    
    def get_queryset(self):
        qs = super().get_queryset()
        try:
            college_id = int(self.kwargs['college_id'])
        except:
            college_id = None
        try:
            player_id = int(self.kwargs['player_id'])
        except:
            player_id = None
        college = 1
        player = 1
        if not college_id is None:
            college = (College.objects.filter(pk=college_id)[0])
            ql = qs.filter(college=college).order_by('?')
        if not player_id is None:
            player = (Player.objects.filter(pk=player_id)[0])
            ql = qs.filter(name=player).order_by('?')
        return ql


def iframe(request, id):
    article = Article.objects.filter(pk=id)[0]
    dont_work = ['espn', 'cbssports', 'nypost']
    display = (not (article.iframe == 'F')
               ) and not ('espn' in str(article.link)) and not ('cbssports' in str(article.link)) and not ('nypost' in str(article.link))
    if not display:
        return redirect(article.link)
    return render(request, 'cfbtimemachine/iframe.html', context={'url': article.link, 'display': display})
