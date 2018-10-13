from django.shortcuts import render
from member.forms import UserForm,MemberForm

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from bar.models import Bar
from member.models import MemberProfile

@login_required
def member_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def index(request):

    if request.user.is_authenticated:
        list = Bar.objects.filter(Creator=MemberProfile.objects.filter(user=request.user)[0])
        return render(request,'member/index.html',{'list':list})

    else:
        return member_login(request)

def member_login(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return render(request,'member/login.html')
        else:
            return render(request,'member/login.html')
    else:
        return render(request,'member/login.html')

def member_register(request):

    registered = False

    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = MemberForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            profile.save()

            registered = True

        else:

            print(user_form.errors, profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = MemberForm()

    return render(request, 'member/registration.html',
                            {   'user_form': user_form,
                                'profile_form' : profile_form,
                                'registered' : registered })
