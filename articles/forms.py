from django import forms
from .models import Commentpost
from captcha.fields import CaptchaField





class CommentForm(forms.ModelForm):
    captcha = CaptchaField()

    class Meta:
        model = Commentpost
        fields = ['name' , 'email', 'message', 'post']
