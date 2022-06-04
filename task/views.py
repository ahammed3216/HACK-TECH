from django.shortcuts import redirect, render
from .forms import LoginForm,SignUpForm,ComplaintForm
from django.contrib.auth import get_user_model,authenticate,login
from .models import Complaint


# Create your views here.
User=get_user_model()

def home(request):
    return render (request,"home.html")

def login_view(request):
    form=LoginForm(request.POST or None)
    if form.is_valid():      
        username=form.cleaned_data.get('username')
        password=form.cleaned_data.get('password')        
        print(form.cleaned_data)
        user=authenticate(username=username,password=password)
        print(user)
        if user is not None:
            
            login(request,user)
            print("sucess")
            return redirect('/')

    return render(request,"login_new.html",{'form':form})

def signup(request):
    form=SignUpForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
        username=form.cleaned_data.get('username')
        email=form.cleaned_data.get('email')
        password=form.cleaned_data.get('password_one')
        print(form.errors)
        User.objects.create_user(
            username=username,email=email,password=password
            )

        return redirect('/')


    return render (request,"sign_up.html",{'form':form})


def complaint(request):
    form=ComplaintForm(request.POST or None)
    if form.is_valid():
        complaint=Complaint()
        print(form.cleaned_data)
        title=form.cleaned_data.get('title')
        institution=form.cleaned_data.get('institution')
        roll_number=form.cleaned_data.get('roll_number')
        description=form.cleaned_data.get('description')
        complaint=Complaint(
            user=request.user,
            title=title,
            institution=institution,
            description=description,
            roll_number=roll_number,
        
        )
        complaint.save()
    return render(request,"complaint.html",{'form':form})