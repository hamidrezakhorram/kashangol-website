from django import forms
from .models import Commentproduct
from captcha.fields import CaptchaField





class CommentForm(forms.ModelForm):
    captcha = CaptchaField()

    class Meta:
        model = Commentproduct
        fields = ['name' , 'email', 'message', 'product']
