from django.shortcuts import render

from articles.models import Article


def articles_list(request):
    template = 'articles/news.html'

    articles = Article.objects.all()

    # for article in articles:
        # article.scopes.order_by('is_main')

    context = {'object_list': articles}

    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/3.1/ref/models/querysets/#django.db.models.query.QuerySet.order_by
    # ordering = '-published_at'

    return render(request, template, context)
