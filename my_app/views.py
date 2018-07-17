from django.shortcuts import render

def home(request):
    context = {}
    template = 'home.html'
    return render(request, template, context)

def about(request):
    context = {}
    template = 'about.html'
    return render(request, template, context)

def contact(request):
    context = {}
    template = 'contact.html'
    return render(request, template, context)
