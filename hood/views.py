from hood.models import Bussiness, Neighbourhood, Post, Profile
from hood.form import BusinessForm, NeighbourHoodForm, PostForm, ProfileForm,  SignUpForm, UserUpdateForm
from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, HttpResponseRedirect, redirect, get_object_or_404
# Create your views here.
def index(request):
    all_hoods = Neighbourhood.objects.all()
    all_hoods = all_hoods[::-1]
    return render(request, 'index.html',{'all_hoods': all_hoods,'all_hoods':all_hoods})

def registration(request):
    if request.method=="POST":
        form=SignUpForm(request.POST) 
        if form.is_valid():
           form.save()
           username = form.cleaned_data.get('username')
           user_password = form.cleaned_data.get('password1')
           user = authenticate(username=username, password=user_password)
           login(request, user)
        return redirect('login')
    else:
        form= SignUpForm()
    return render(request, 'registration/registration_form.html', {"form":form}) 

@login_required(login_url='/accounts/login/')
def add_neighbourhood(request):
    if request.method == 'POST':
        form = NeighbourHoodForm(request.POST, request.FILES)
        if form.is_valid():
            neighbourhood = form.save(commit=False)
            neighbourhood.admin = request.user
            neighbourhood.save()
            messages.success(
                request, 'You have succesfully created a Neighbourhood.Now proceed and join the Neighbourhood')
            return redirect('index')
    else:
        form = NeighbourHoodForm()
    return render(request, 'hood.html', {'form': form})

@login_required(login_url='/accounts/login/')    
def profile(request):
    if request.method == 'POST':

        userForm = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileForm(
            request.POST, request.FILES, instance=request.user)

        if  profile_form.is_valid():
            profile_form.save()

            return redirect('home')

    else:
        profile_form = ProfileForm(instance=request.user)
        user_form = UserUpdateForm(instance=request.user)

        params = {
            'user_form':user_form,
            'profile_form': profile_form

        }
    return render(request, 'profile.html', params)

@login_required(login_url='/accounts/login/')
def join_neighbourhood(request, id):
    profile= Profile.objects.get_or_create(user=request.user)
    neighbourhood = get_object_or_404(Neighbourhood, id=id)
    request.user.profile.neighbourhood = neighbourhood
    request.user.profile.save()
    messages.success(
        request, 'You have succesfully joined this Neighbourhood ')
    return redirect('index')



@login_required(login_url='/accounts/login/')
def single_neighbourhood(request, hood_id):
    neighbourhood = Neighbourhood.objects.get(id=hood_id)
    business = Bussiness.objects.filter(neighbourhood_id=hood_id)
    posts = Post.objects.filter(neighbourhood=neighbourhood)
    posts = posts[::-1]
    if request.method == 'POST':
        form = BusinessForm(request.POST)
        if form.is_valid():
            b_form = form.save(commit=False)
            b_form.neighbourhood = neighbourhood
            b_form.user = request.user.profile
            b_form.save()
            return redirect('single-hood',hood_id)
    else:
        form = BusinessForm()
    context = {
        'neighbourhood': neighbourhood,
        'form': form,
        'posts': posts,
        'business': business,

    }
    return render(request, 'single_hood.html', context)

@login_required(login_url='/accounts/login/')
def leave_neighbourhood(request, id):
    neighbourhood = get_object_or_404(Neighbourhood, id=id)
    request.user.profile.neighbourhood = None
    request.user.profile.save()
    messages.success(
        request, 'Success! You have succesfully exited this Neighbourhood ')
    return redirect('index')


@login_required(login_url='/accounts/login/')
def create_post(request, hood_id):
    neighbourhood = Neighbourhood.objects.get(id=hood_id)
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.neighbourhood = neighbourhood
            post.user = request.user.profile
            post.save()
            messages.success(
                    request, 'You have succesfully created a Post')
            return redirect('single-hood', neighbourhood.id)
    else:
        form = PostForm()
    return render(request, 'post.html', {'form': form})


@login_required(login_url='/accounts/login/')
def search_business(request):
    if request.method == 'GET':
        name = request.GET.get("title")
        results = Bussiness.objects.filter(name__icontains=name).all()
        print(results)
        message = f'name'
        context = {
            'results': results,
            'message': message
        }
        return render(request, 'search.html', context)
    else:
        message = "You haven't searched for any business"
    return render(request, "search.html")
