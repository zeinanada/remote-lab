from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import subprocess
# Create your views here.

@login_required()
def stream(request):
    return render(request,'camera.html')

@login_required(login_url="/login/")
def motion_stream(request):
    #subprocess.Popen(['motion'])
    #subprocess.call('./sleep.sh')
    return render(request,'motioncamera.html')


