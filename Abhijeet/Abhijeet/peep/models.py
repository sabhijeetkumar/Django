from django.db import models
from django.contrib.auth.models import User

class Peep(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="User")
    text = models.TextField(max_length=240, verbose_name="Text")
    photo = models.ImageField(upload_to='photos/', blank=True, null=True, verbose_name="Photo")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At", db_index=True)
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")
    
    class Meta:
        verbose_name = "Peep"
        verbose_name_plural = "Peeps"
        ordering = ['-created_at']  # Latest first by default
    
    def __str__(self):
        return f'{self.user.username} - {self.text[:20]}'
