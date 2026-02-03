from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from .models import ShortenedURL
from .forms import URLShortenForm, EditShortURLForm, ExpireURLForm
import string
import random
# from django.core.paginator import Paginator
from django.utils import timezone
from datetime import timedelta



# Create your views here.

def home(request):
    return render(request, 'home.html')

def register_view(request):
    if request.method == 'POST':
        firstname=request.POST.get('firstname')
        lastname=request.POST.get('lastname')
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        cpassword=request.POST.get('confirm_password') 
        register_error = False

        if User.objects.filter(username=username).exists():
            register_error = True
            messages.error(request, "Username already exists")
        if not email.endswith('@gmail.com'):
            register_error = True
            messages.error(request, "invalid email address")


        if User.objects.filter(email=email).exists():
            register_error = True
            messages.error(request, "Email already exists")

        if len(password) < 5:
            register_error = True
            messages.error(request, "Password must be at least 5 characters")
        if password != cpassword:
            register_error = True
            messages.error(request, "Passwords do not match")

        if register_error:
            return redirect('register')
        else:
            new_user = User.objects.create_user(
                first_name=firstname,
                last_name=lastname,
                email=email, 
                username=username,
                password=password
            )
            messages.success(request, "Account created. Login now")
            return redirect('login')

        

    return render(request, 'register.html')

def login_view(request):
    if request.method == 'POST':
        # email=request.POST.get('email')
        username=request.POST.get('username')

        password=request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            return redirect('home')
        
        else:
            messages.error(request, "Invalid login credentials")
            return redirect('login')
    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('home')

@login_required(login_url='login')
def shorten_url(request):
    form = URLShortenForm() 
    
    if request.method == 'POST':
        form = URLShortenForm(request.POST) 
        if form.is_valid():
            url = form.cleaned_data['original_url']
            
            char_set = string.ascii_letters + string.digits
            while True:
                random_code = ''.join(random.choices(char_set, k=6))
                if not ShortenedURL.objects.filter(short_url=random_code).exists():
                    break
            
            obj = form.save(commit=False)
            obj.user = request.user
            obj.short_url = random_code 
            obj.save()
            
            messages.success(request," URL shortened successfully!")
            return redirect('shorten_url') 
    user_urls = ShortenedURL.objects.filter(user=request.user).order_by('-created_at')
    # paginator = Paginator(user_urls, 3)
    context = {
        'form': form,
        'obj': user_urls,
        # 'paginator': paginator
    }
    return render(request, 'shorten_url.html', context)

def redirect_url(request, short_url):
    try:
        url_obj= ShortenedURL.objects.get(short_url=short_url)
        url_obj.counter+= 1
        url_obj.last_clicked = timezone.now()
        url_obj.save()
        return redirect(url_obj.original_url)
       
    except ShortenedURL.DoesNotExist:
        return render(request, 'pagenotfound.html', status=404)
    

def page_not_found(request, exception):
    return render(request, 'pagenotfound.html', status=404)


@login_required(login_url='login')
def delete_url(request, u_id):
    url =get_object_or_404(ShortenedURL, id=u_id, user=request.user)
    if request.method == "POST":
        url.delete()
        messages.success(request, " URL deleted successfully ")
        return redirect('shorten_url')
    
    return render(request, 'deleteurl.html', {'url': url})

@login_required(login_url='login')
def edit_url(request, u_id):
    url = get_object_or_404(ShortenedURL, id=u_id, user=request.user)
    form = EditShortURLForm(instance=url)
    
    if request.method == "POST":
        form = EditShortURLForm(request.POST, instance=url)
        if form.is_valid():
            form.updated_at=timezone.now()
            form.save()
            messages.success(request, " Short URL updated successfully ")
            return redirect('shorten_url')

    return render(request, 'editshorturl.html', {'form': form, 'url': url})

def qr_code_view(request, u_id):
    url = get_object_or_404(ShortenedURL, id=u_id, user=request.user)
    qr_code_data = url.qr_code()
    context = {
        'qr_code_data': qr_code_data,
        'short_url': url.short_url
    }
    return render(request, 'qr_code.html', context)

@login_required(login_url='login')
def expire_url(request, u_id):
    url = get_object_or_404(ShortenedURL, id=u_id, user=request.user)
    
    if request.method == "POST":
        form = ExpireURLForm(request.POST, instance=url)
        if form.is_valid():
            obj = form.save(commit=False)
            hours = int(form.cleaned_data['expires_at'])
            if hours > 0:
                obj.expires_at = timezone.now() + timedelta(hours=hours)
            else:
                obj.expires_at = None
            
            obj.save()
            messages.success(request, "Expiration set successfully!")
            return redirect('shorten_url')
    else:
        form = ExpireURLForm(instance=url)

    return render(request, 'expire.html', {'form': form, 'url': url})

from django.db.models import Q
def profile(request, u_id):
    q=request.GET.get('q') if request.GET.get('q')!=None else ''
    user_urls = ShortenedURL.objects.filter(Q(short_url__icontains=q), user=request.user).order_by('-created_at')
    total=user_urls.count()
    return render(request,"profile.html",{"url":user_urls,"total":total})
