from django.shortcuts import redirect, render
from .models import Article
from django.views.generic import ListView
from django.utils.http import urlencode
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

    def get_queryset(self):
        qs = super().get_queryset()
        ql = list(qs.exclude(img='nan').order_by('?')) + \
            list(qs.filter(img='nan'))
        return ql


def iframe(request, id):
    article = Article.objects.filter(pk=id)[0]
    dont_work = ['espn', 'cbssports', 'nypost']
    display = (not (article.iframe == 'F')
               ) and not ('espn' in str(article.link)) and not ('cbssports' in str(article.link)) and not ('nypost' in str(article.link))
    if not display:
        return redirect(article.link)
    return render(request, 'cfbtimemachine/iframe.html', context={'url': article.link, 'display': display})
