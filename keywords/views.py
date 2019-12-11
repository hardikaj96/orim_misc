from django.shortcuts import render

# Create your views here.
from keywords.models import Keywords, TitlesGeneral

def keyword_index(request):
    keywords = Keywords.objects.all()
    context = {
        'keywords': keywords
    }
    return render(request, 'keyword_index.html', context)

def keyword_details(request, kw):
    details = TitlesGeneral.objects.all().filter(keyword=kw)
    context = {
        'details': details
    }
    return render(request, 'keyword_details.html', context)