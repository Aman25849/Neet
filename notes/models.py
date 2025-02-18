from django.db import models

# Create your models here.

class Messages(models.Model):
    user = models.CharField(max_length=15)
    messages = models.CharField(max_length=300)
    time_date = models.DateTimeField(auto_now=True)
   
    
    def __str__(self):
        return self.messages[0:15]