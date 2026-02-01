from .models import ShortenedURL
from django import forms


class URLShortenForm(forms.ModelForm):
    class Meta:
        model = ShortenedURL
        fields = ['original_url']   
        widgets = {
            'original_url': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Enter URL to shorten'}),
        }
        