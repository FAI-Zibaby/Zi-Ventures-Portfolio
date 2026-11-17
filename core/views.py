from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def home(type_request):
    context = {
        'brand_name': 'The Zi Ventures',
        'tagline': 'Software Engineering, Graphic Design, & Digital Solutions',
    }
    return render(type_request, 'core/index.html', context)