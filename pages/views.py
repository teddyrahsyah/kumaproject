from django.shortcuts import render

from .models import HomepageImage, ServicepageImage, AboutpageImage, JoinpageImage

# Create your views here.
def homepage(request):
    context = {
        'benefits': HomepageImage.objects.all()[:4],
        'mobileapp': HomepageImage.objects.last()
    }
    return render(request, 'pages/index.html', context)

def servicepage(request):
    consumer_data = ServicepageImage.objects.all()
    context = {
        'consumers': consumer_data
    }
    return render(request, 'pages/service.html', context)

def aboutpage(request):
    context = {
        'first': AboutpageImage.objects.first(),
        'creators': AboutpageImage.objects.all(),
        'last': AboutpageImage.objects.get(id=2)
    }
    return render(request, 'pages/about.html', context)


content = JoinpageImage.objects.all()
def join_produsen(request):
    context = {
        'join': content[0],
        'sell': content[1],
        'finance': content[2],
        'mobileapp': content[6],
    }
    return render(request, 'pages/join_produsen.html', context)


def join_supplier(request):
    context = {
        'join': content[3],
        'sell': content[4],
        'finance': content[5],
        'mobileapp': content[6],
    }
    return render(request, 'pages/join_supplier.html', context)
