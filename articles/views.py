from urllib.parse import urlencode, quote_plus

from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import get_object_or_404, render

from .models import Article

OPEN = 0
SKIPPED = 1
SHARED = 2
MAX_ENTRIES = 100
TWITTER_INTENT = 'https://twitter.com/intent/tweet?'


def index(request):
    articles = Article.objects.order_by('-published')[:MAX_ENTRIES]
    template = loader.get_template('articles/index.html')
    context = {
        'title': 'Articles',
        'articles': articles,
    }
    return HttpResponse(template.render(context, request))


def detail(request, article_id):
    article = get_object_or_404(Article, pk=article_id)

    payload = {'text': article.title, 'url': article.url}
    tweet_url = TWITTER_INTENT + urlencode(payload, quote_via=quote_plus)

    return render(request, 'articles/detail.html', 
                  {'title': 'Article Detail',
                   'article': article,
                   'tweet_url': tweet_url})


def _update(request, article_id, status):
    article = get_object_or_404(Article, pk=article_id)
    article.status = status
    # TODO - edited_by
    article.save()
    return HttpResponseRedirect('/articles')


def skip(request, article_id):
    return _update(request, article_id, SKIPPED)


def share(request, article_id):
    return _update(request, article_id, SHARED)
