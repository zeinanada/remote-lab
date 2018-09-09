from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from bootstrap_datepicker.widgets import DatePicker
import time
from datetime import datetime,timedelta


class DateInput(forms.DateInput):
    input_type = 'date'
    
class TimeInput(forms.TimeInput):
    input_type = 'time'

class RegisterForm(forms.Form):
    date = forms.DateField(widget= DateInput(),help_text="Choose date, must be in the present")
    start  = forms.TimeField(widget= TimeInput(), help_text="Start session time, must be in the present")
    finish = forms.TimeField(widget= TimeInput(), help_text="End session time,  must be in the present")

    def clean_date(self):
        cleaned_data = super().clean()
        date = cleaned_data.get("date")
        if date < date.today()  :
            raise forms.ValidationError("The date cannot be in the past!")        
        return date

    def clean_start(self):
        cleaned_data = super().clean()
        date = cleaned_data.get("date")
        start = cleaned_data.get("start")
        now = datetime.now().strftime('%H:%M')
        if str(start)< now and date == date.today():
            
            raise forms.ValidationError("Start  time cannot be in the past!")
            
        return start

    def clean_finish(self):
        cleaned_data = super().clean()
        date = cleaned_data.get("date")
        finish = cleaned_data.get("finish")
        now = datetime.now().strftime('%H:%M')
        if cleaned_data.get("start") is None: 
            start = datetime.now()
        else: 
            start = cleaned_data.get("start")
        
        s = timedelta(hours=start.hour, minutes=start.minute, seconds=start.second, microseconds=start.microsecond)
        f = timedelta(hours=finish.hour, minutes=finish.minute, seconds=finish.second, microseconds=finish.microsecond)
        if str(finish)< now and date == date.today():
            raise forms.ValidationError("Finish  time cannot be in the past!")       
        if f> s+timedelta(minutes=6*60) :
            raise forms.ValidationError("Duration can not be more than 6 hours!") 
        if f<s:
            raise forms.ValidationError("Finish time can not be before start time!") 
        return finish


