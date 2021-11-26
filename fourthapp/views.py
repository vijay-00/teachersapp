from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from fourthapp.models import loandetails, memberdetails, profiledetails, transactions, outstanding
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.sessions.models import Session


# Create your views here.
def loginpage(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        global loanid, memberid, profileloanid, transid, osid
        loanid = request.POST['userid']
        memberid = request.POST['userid']
        profileloanid = request.POST['userid']
        transid = request.POST['userid']
        osid = request.POST['userid']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('homepage')
        else:
            messages.success(request, (' please enter valid username and password'))
            return redirect('loginpage')

    return render(request, 'fourthapp/loginpage.html')


# def loginpage(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         global loanid, memberid, profileloanid, transid, osid
#         loanid = request.POST['username']
#         memberid = request.POST['username']
#         profileloanid = request.POST['username']
#         transid = request.POST['username']
#         osid = request.POST['username']
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect('homepage')
#         else:
#             messages.success(request, (' please enter valid username and password'))
#             return redirect('loginpage1')
#
#     return render(request, 'fourthapp/loginpage1.html')


@login_required(login_url='loginpage')
def homepage(request):
    loandata = loandetails.objects.filter(userid=loanid)
    memberdata = memberdetails.objects.filter(userid=memberid)
    transdata = transactions.objects.filter(userid=transid)
    osdata = outstanding.objects.filter(userid=osid)
    return render(request, 'fourthapp/homepage.html',
                  context={'loandata': loandata, 'transdata': transdata, 'osdata': osdata, 'memberdata': memberdata})


@login_required(login_url='loginpage')
def profilepage(request):
    profiledata = profiledetails.objects.filter(userid=memberid)
    profileloandata = loandetails.objects.filter(userid=profileloanid)
    return render(request, 'fourthapp/profilepage.html',
                  {'profiledata': profiledata, 'profileloandata': profileloandata})


def registerpage(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('loginpage')
    else:
        form = UserCreationForm()

    return render(request, 'fourthapp/registerpage.html', {'form': form})


@login_required(login_url='loginpage')
def logoutuser(request):
    logout(request)
    messages.success(request, ('you are logged out'))
    return redirect('loginpage')


#
# def outpage(request):
#     return render(request, 'fourthapp/out.html')
def index(request):
    return render(request, 'fourthapp/index.html')
