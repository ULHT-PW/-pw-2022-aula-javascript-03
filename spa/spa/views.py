from django.shortcuts import render
from django.http import HttpResponse


def index_view(request):
    return render(request, 'spa/index.html')


texts = [
    'Página com texto da secção 1',
    'Página com texto da secção 2',
    'Página com texto da secção 3',
    ]


def section_view(request, section):
    if 1 <= section <= 3:
        return HttpResponse(texts[section-1])
    else:
        return HttpResponse('secção inexistente')

