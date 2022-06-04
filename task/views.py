from django.shortcuts import redirect, render
from .forms import LoginForm,SignUpForm,ComplaintForm,JobForm
from django.contrib.auth import get_user_model,authenticate,login
from .models import Complaint,ApplyOppurtunity


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


    return render (request,"signup.html",{'form':form})


def complaint(request):
    form=ComplaintForm(request.POST or None)
    if form.is_valid():
        complaint=Complaint()
        print(form.cleaned_data)
        title=form.cleaned_data.get('title')
        institution=form.cleaned_data.get('institution')
        roll_number=form.cleaned_data.get('roll_number')
        description=form.cleaned_data.get('description')
        email=form.cleaned_data.get('email')
        complaint=Complaint(
            user=request.user,
            title=title,
            institution=institution,
            description=description,
            roll_number=roll_number,
            email=email
        
        )
        complaint.save()
        return redirect('/')
    return render(request,"complaint_n.html",{'form':form})


def job(request):
    form=JobForm(request.POST or None)
    if form.is_valid():
        job_model=ApplyOppurtunity()
        print(form.cleaned_data)
        name=form.cleaned_data.get('name')
        institution=form.cleaned_data.get('institution')
        email=form.cleaned_data.get('email')
        description=form.cleaned_data.get('description')
        contact_number=form.cleaned_data.get('contact_number')

        job_model=ApplyOppurtunity(
            user=request.user,
            name=name,
            institution=institution,
            email=email,
            description=description,
            contact_number=contact_number
        )

        job_model.save()

        return redirect('/')


    return render(request,"job.html")