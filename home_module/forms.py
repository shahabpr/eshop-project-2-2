from django import forms


class ContactUsForm(forms.Form):
    fullname=forms.CharField(label='نام و نام خانوادگی', max_length=200)
    email=forms.EmailField(label='ایمیل', max_length=200)
    subject=forms.CharField(label='عنوان', max_length=200)
    message=forms.CharField(label='متن پیام')

