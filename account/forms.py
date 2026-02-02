from .models import ShortenedURL
from django import forms


class URLShortenForm(forms.ModelForm):
    class Meta:
        model = ShortenedURL
        fields = ['original_url']   
        widgets = {
            'original_url': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Enter URL to shorten'}),
        }
class EditShortURLForm(forms.ModelForm):
    class Meta:
        model = ShortenedURL
        fields = ['short_url']   
        widgets = {
            'short_url': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the desired short URL'}),
        }
        