from django import forms
from website.models import Newsletter


class Newsletterform(forms.ModelForm):


    class Meta:
        model = Newsletter
        fields = '__all__'