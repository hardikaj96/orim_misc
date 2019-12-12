from django.shortcuts import render

# Create your views here.
from keywords.models import Keywords, TitlesGeneral, OrimTitles

def keyword_index(request):
    keywords = Keywords.objects.all()
    context = {
        'keywords': keywords
    }
    return render(request, 'keyword_index.html', context)

def keyword_details(request, kw):
    details = TitlesGeneral.objects.all().filter(keyword=kw)
    orim_title_details = OrimTitles.objects.raw('select * FROM keywords_OrimTitles as ot, keywords_TitlesGeneral as tg WHERE ot.asin = tg.asin and tg.keyword = %s',[kw]) 
    print(orim_title_details)
    context = {
        'details': details,
        'orim_title_details': orim_title_details
    }
    return render(request, 'keyword_details.html', context)