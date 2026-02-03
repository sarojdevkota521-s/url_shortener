from django.db import models
from django.contrib.auth.models import User
import qrcode
import io
import base64
from django.utils import timezone

# Create your models here.
class ShortenedURL(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    original_url = models.URLField()
    short_url = models.CharField(max_length=20, unique=True)
    counter = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    last_clicked=models.DateTimeField(blank=True, null=True)
    expires_at = models.DateTimeField(blank=True, null=True)


    def __str__(self):
        return f"{self.original_url} - by {self.user.username}"
    def qr_code(self):
        qr=qrcode.QRCode(version=1, box_size=10, border=5)
        qr.add_data(self.short_url)
        qr.make(fit=True)
        img=qr.make_image(fill='black', back_color='white')
        buffer=io.BytesIO() 
        img.save(buffer, format='PNG')
        img_str=base64.b64encode(buffer.getvalue()).decode()
        return img_str
    
    def is_expired(self):
        if self.expires_at and timezone.now() > self.expires_at:
            return True
        return False
    
    
    