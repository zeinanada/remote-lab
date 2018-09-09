from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#class Document(models.Model):
#    description = models.CharField(max_length=255, blank=True)
#    document = models.FileField(upload_to='documents/')
#    uploaded_at = models.DateTimeField(auto_now_add=True)
#    author = models.ForeignKey(User, default=None,on_delete=models.CASCADE)
#    
#    def __str__(self):
#        return self.description

#class Upload(models.Model):
#    Bitstream = models.FileField(upload_to='Bitstream/')
#    probs = models.FileField(upload_to='probs/')
#    uploaded_at = models.DateTimeField(auto_now_add=True)
#    author = models.ForeignKey(User, default=None,on_delete=models.CASCADE)
#    
#    def __str__(self):
#        return self.uploaded_at

