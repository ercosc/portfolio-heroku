from django.shortcuts import render


# Create your views here.
def start_page(request):
    return render(request, 'start_page.html')


def work_page(request):
    return render(request, 'work_page.html')


def service_page(request):
    return render(request, 'service_page.html')


def about_page(request):
    return render(request, 'about_page.html')


def blog_page(request):
    return render(request, 'blog_page.html')


def contact_page(request):
    return render(request, 'contact_page.html')
