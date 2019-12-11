from django.shortcuts import render

# Create your views here.

def search_keywords(request):
    return render(request, 'search.html', {})