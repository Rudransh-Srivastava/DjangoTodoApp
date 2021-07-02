from django.db import models
from django.contrib.auth.models import User
from django.db.models.expressions import OrderBy

# Create your models here.
class Tasks(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE, null=True,blank=True)
    title= models.CharField(max_length=200)
    desc= models.TextField(null=True)
    complete= models.BooleanField(default=False)
    created= models.DateTimeField(auto_now_add=True) #This is automatiaclly save the date-time .

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['complete']

