from app import app
from flask import render_template
import subprocess
from flask import request
import json 

@app.route('/index')
def index():
    user = {'username': 'Zeina'}
    return render_template('index.html', title='index', user=user)


@app.route('/',methods=['GET', 'POST'])
def home():
    print(request.get_data())
    data = json.loads(request.get_data())
    subprocess.call(['sudo','./user_add.sh',data["username"],data["password"]])
    user = {'username':'your script is done'}
    return render_template('index.html', title='call script', user=user)
    
@app.route('/switch',methods=['GET', 'POST'])
def switch():
    data = json.loads(request.get_data())
    print(data)
    if data["state"] == '1':
        subprocess.call(['./echo1.sh'])
    else:
        subprocess.call(['./echo0.sh'])
    user = {'username': data["state"]}
    return render_template('index.html', title='got state', user=user)

@app.route('/register',methods=['GET', 'POST'])
def register():
    data = json.loads(request.get_data())
    subprocess.call(['./grant_user_timeslot.sh',data["username"],data["start_datetime"],data["finish_datetime"]])
    user = {'username': data["username"]}
    return render_template('index.html', title='Register for user', user=user)


