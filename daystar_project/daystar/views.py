from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'daystar/home.html')


def about(request):
    return render(request,'daystar/about.html')


def contact(request):
    return render(request,'daystar/contact.html')


def blog(request):
    return render(request,'daystar/blog.html')