from django import forms
from .models import Reservation

class ReservationForm(forms.ModelForm):
    def clean_name(self):
            name = self.cleaned_data['name']
            return f'{name.upper()}'

    class Meta:
        

        
        model = Reservation
        fields = ('name', 'phone', 'email', 'date', 'time', 'count', 'comment')

        widgets = {
            "name" : forms.TextInput(attrs={"class": "form-control", "id" : "name", "placeholder": "Your Name", "data-rule" : "minlen:4"}),
            "phone" : forms.TextInput(attrs={"class": "form-control", "id" : "phone", "placeholder" : "Your Phone", "data-rule" : "minlen:9"}),
            "email" : forms.EmailInput(attrs={"class":"form-control", "id" : "email", "placeholder" : "Your Email", "data-rule" : "email"}),
            "date" : forms.DateInput(attrs={"class": "form-control", "id" : "date", "placeholder" : "Date", "data-rule" : "minlen:4"}),
            "time" : forms.TimeInput(attrs={"class": "form-control", "id" : "time", "placeholder" : "Time", "data-rule" : "minlen:4"}),
            "count" : forms.NumberInput(attrs={"class": "form-control", "id" : "count", "placeholder" : "Number of people", "data-rule" : "minlen:1"}),
            "comment" : forms.Textarea(attrs={"class": "form-control","id" : "comment", "rows" : "5","placeholder" : "Message" })
        }

        labels = {
            'name': 'Name',
            'phone': 'Phone',
            'email': 'Email',
            'date': 'Date',
            'time': 'Time',
            'count': 'Count',
            'comment': 'Comment',
        }
        help_texts = {
            'phone': 'Enter the phone number in the format : +380XXXXXXXXX',
        }
        error_messages = {
            'name': {
                'required': 'This field is required',
            },
            'phone': {
                'required': 'This field is required',
            },
            'email': {
                'required': 'This field is required',
            },
            'date': {
                'required': 'This field is required',
            },
            'time': {
                'required': 'This field is required',
            },
            'count': {
                'required': 'This field is required',
            },
        }