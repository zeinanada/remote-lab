from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.http import HttpResponse
from django.contrib.auth import login, logout,authenticate
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User
from django.contrib import messages
import subprocess
import urllib.request
import json

def signup_view(request):
    if request.method == 'POST':       
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            user_info = {"username": username,"password": raw_password}
            data = json.dumps(user_info)
            byte_data = data.encode('utf8')
            request = urllib.request.Request('http://127.0.0.1:5000/', byte_data)
            with urllib.request.urlopen(request) as response:
                html = response.read()
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request,'accounts/signup.html',{'form':form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return render(request, 'home.html')            
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', { 'form': form })

def logout_view(request):
    logout(request)
    return render(request, 'accounts/logout.html')


@login_required(login_url="/login/")
def upload_view(request):
    if request.method == 'POST' and request.FILES['Bitstream'] and request.FILES['probs'] :
        if 'upload_btn' in request.POST:
            Bitstream = request.FILES['Bitstream']
            probs = request.FILES['probs']
            fs = FileSystemStorage()
            Bitstream_filename = fs.save(Bitstream.name, Bitstream)
            probs_filename = fs.save(probs.name, probs)
            uploaded_file_url_Bitstream = fs.url(Bitstream_filename)
            uploaded_file_url_probs = fs.url(probs_filename) 
            return render(request, 'form_upload.html', {'uploaded_file_url_Bitstream': uploaded_file_url_Bitstream,'uploaded_file_url_probs' : uploaded_file_url_probs})  
        if 'execute_btn' in request.POST:
            if request.session.get('date') is None:
                messages.warning(request, 'Please register time slice first.',extra_tags='alert')
                return render(request, 'form_upload.html')
            else:
                print("date was set")
                print(request.session['date'])

    return render(request, 'form_upload.html')


#request.session['order_no']=order_no
@login_required(login_url="/login/")
def Register_timeslice_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST) 
        if form.is_valid() :
            date = form.cleaned_data['date']
            print(date)
            start = form.cleaned_data['start']
            print(start)
            finish = form.cleaned_data['finish']
            print(finish)
            request.session['date']= str(date)          
            s_h = '0'+str(start.hour) if start.hour<10 else str(start.hour)
            s_m = '0'+str(start.minute) if start.minute<10 else str(start.minute)
            start_datetime = s_h +':'+ s_m + ' '+str(date)

            f_h = '0'+str(finish.hour) if finish.hour<10 else str(finish.hour)
            f_m = '0'+str(finish.minute) if finish.minute<10 else str(finish.minute)
            finish_datetime = f_h +':'+ f_m + ' '+str(date)

            print(start_datetime)
            print(finish_datetime)
            user = User.objects.get(pk=request.user.id)
            print(user.username)
            print(user.password)   
            info = {"username": user.username,"start_datetime": start_datetime, "finish_datetime":finish_datetime}
            data = json.dumps(info)
            byte_data = data.encode('utf8')
            request = urllib.request.Request('http://127.0.0.1:5000/register', byte_data)         
            with urllib.request.urlopen(request) as response:
                html = response.read()
            return redirect('home')
            

        if 'next' in request.POST:
            return redirect(request.POST.get('next'))
        else:
            render(request,'accounts/register.html',{'form':form})

    else:
        form = RegisterForm()
    return render(request,'accounts/register.html',{'form':form})



#@login_required(login_url="/login/")
#def model_form_upload_view(request):
#    if request.method == 'POST':
#        form = forms.DocumentForm(request.POST, request.FILES)
#        if form.is_valid():
#            instance = form.save(commit=False)
#            #instance = ModelWithFileField(file_field=request.FILES['file'])
#            instance.author = request.user
#            instance.save()
#            return redirect('home')
#    else:
#        form = forms.DocumentForm()
#    return render(request, 'form_upload.html', {
#        'form': form
#    })

#def show_files(request):
#    files = Upload.objects.all()
#    return render(request,'files.html')
