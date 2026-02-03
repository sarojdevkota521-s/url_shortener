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
CHOICES = [
    (0, 'Never'),
    (1, '1 Hour'),
    (24, '1 Day'),
    (48, '2 Days'),
    (168, '1 Week'),
    (720, '1 Month'),
]

class ExpireURLForm(forms.ModelForm):
    expires_at = forms.ChoiceField(
        choices=[
            (0, 'Never'),
            (1, '1 Hour'),
            (2, '2 Hours'),
            (6, '6 Hours'),
            (12, '12 Hours'),
            (24, '1 Day'),
            (48, '2 Days'),
            (72, '3 Days'),
            (168, '1 Week'),
        ],
        label="Select Expiration Time"
    )
    class Meta:
        model = ShortenedURL
        fields = []
   