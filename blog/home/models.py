from django.db import models

# Create your models here.
class blog(models.Model):
    image=models.ImageField(null=True, blank=True,)
    heading=models.CharField(max_length=100, null=True)
    brief=models.CharField(max_length=100000, null=True)
    author=models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.author