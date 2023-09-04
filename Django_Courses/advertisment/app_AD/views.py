from django.shortcuts import render, redirect
from .models import AD
from .forms import ADForm
from django.urls import reverse


def index(request):
    ads = AD.objects.all()
    context = {'ads':ads}
    return render(request, 'index.html', context)


def top_sellers(request):
    return render(request, 'top-sellers.html')


def advertisement_post(request):
    if request.method == 'POST':
        form = ADForm(request.POST, request.FILES)
        if form.is_valid():
            ad = AD(**form.cleaned_data)
            ad.user = request.user
            ad.save()
            url = reverse('main_page')
            return redirect(url)
    else:    
        form = ADForm()
    context = {'form': form}
    return render(request, 'advertisement-post.html', context)


def register(request):
    return render(request, 'register.html')


def login(request):
    return render(request, 'login.html')


def profile(request):
    return render(request, 'profile.html')