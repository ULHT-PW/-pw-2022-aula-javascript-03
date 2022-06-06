import time
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
def index_view(request):
    return render(request, 'scroll/index.html')


def posts_view(request):
    start = int(request.GET.get('start') or 0)
    end = int(request.GET.get('end') or (start + 9))

    # gerar lista de posts
    data = [f'Post #{i}' for i in range(start, end+1)]

    # atrasar a resposta artificialmente
    time.sleep(1)

    return JsonResponse({'posts': data})