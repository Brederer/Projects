from django.shortcuts import render, redirect
from .models import AD
from .forms import ADForm
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required


def index(request):
    title = request.GET.get('query')
    if title:
        ads = AD.objects.filter(title=title)
    else: 
        ads = AD.objects.all()
    # ads = AD.objects.all()
    context = {'advertisements':ads}
    return render(request, 'app_AD/index.html', context)


def top_sellers(request):
    return render(request, 'app_AD/top-sellers.html')


@login_required(login_url=reverse_lazy('login'))
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
    return render(request, 'app_AD/advertisement-post.html', context)


def register(request):
    return render(request, 'app_auth/register.html')


def login(request):
    return render(request, 'app_auth/login.html')


def profile(request):
    return render(request, 'app_auth/profile.html')