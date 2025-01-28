from django.http import JsonResponse
from .models import Article

def articles_list(request):
    articles = Article.objects.all().values()
    return JsonResponse(list(articles), safe=False)

def article_detail(request, id):
    try:
        article = Article.objects.get(id=id)
        return JsonResponse({
            'title': article.title,
            'text': article.text,
            'author': article.author
        })
    except Article.DoesNotExist:
        return JsonResponse({'error': 'Article not found'}, status=404)
