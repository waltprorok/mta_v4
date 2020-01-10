from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def pricing(request):
    return render(request, 'pricing.html')


def privacy(request):
    return render(request, 'privacy.html')


def terms(request):
    return render(request, 'terms.html')
