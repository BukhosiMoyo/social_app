from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import LoginForm, UserRegistrationForm, UserEditForm, ProfileEditForm
from django.contrib.auth.decorators import login_required
from .models import Profile
from django.contrib import messages


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Aunthenticated successfully')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    context = {'form':form}
    return render(request, 'accounts/login.html', context)


@login_required
def dashboard(request):
    context={'section': 'dashboard'}
    return render(request, 'accounts/dashboard.html', context)


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            #create a new user but avoude saving it yet
            new_user = user_form.save(commit=False)
            #Now here you are setting thr chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            #now you can save the user object 
            new_user.save()
            Profile.objects.create(user=new_user)
            context = {'new_user':new_user}
            return render(request, "accounts/register_done.html", context)

    else:
        user_form = UserRegistrationForm()
    context = {'user_form':user_form}
    return render(request, "accounts/register.html", context)


@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST, files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Profile updated successfully')

        else:
            messages.error(request, 'Error updating your profile')

    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)

    context ={'user_form': user_form, 'profile_form': profile_form}
    return render(request, "accounts/edit.html", context)


    


