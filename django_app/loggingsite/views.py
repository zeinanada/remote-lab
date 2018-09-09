from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
import urllib.request
import subprocess
import json


def homepage(request):
    if request.method == "POST":
        if request.POST.get('switchx') == "on":
            state = {"state": '1'}
            data = json.dumps(state)
            byte_data = data.encode('utf8')
            urllib.request.urlopen('http://127.0.0.1:5000/switch', byte_data)
            print("on")
        else :
            state = {"state": '0'}
            data = json.dumps(state)
            byte_data = data.encode('utf8')
            urllib.request.urlopen('http://127.0.0.1:5000/switch', byte_data)
            print("off")

        switch = str(request.POST.get('switchesID'))
        print(switch)
        for id in range(int(switch)):
            print('switch' + str(id))
            print(request.POST.get('switch' + str(id)))
        return render(request,'home.html')
    else:    
        return render(request,'home.html')

def about(request):
    return HttpResponse("about")

