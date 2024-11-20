from django.db import models

# Create your models here.
class Blogs(models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField(max_length=200)
    date=models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.title 