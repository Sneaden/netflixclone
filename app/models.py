from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class CustomManager(models.Manager):
    def horror_list(self):
        return self.filter(category__exact="horror")
    
    def comedy_list(self):
        return self.filter(category__exact="comedy")
    
    def science_fiction_list(self):
        return self.filter(category__exact="sciencefiction")
    
    def adult_list(self):
        return self.filter(category__exact="adult")
    
    def thrilling_list(self):
        return self.filter(category__exact="thrilling")
    
    def romance_list(self):
        return self.filter(category__exact="romance")


class Movie(models.Model):
    userid=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    movieid=models.IntegerField(primary_key=True,default=0)
    title = models.CharField(max_length=1000)
    description = models.TextField(blank=True, null=True)
    type =(("horror","horror"),("comedy","comedy"),("sciencefiction","sciencefiction"),("adult","adult"),("thrilling","thrilling"),("romance","romance"))
    category=models.CharField(max_length=60,choices=type)
    image = models.ImageField(upload_to='photos')
    video=models.FileField(upload_to="media/",default=None)
    age_limit = models.CharField(max_length=10)
    objects=models.Manager()
    moviemanager=CustomManager()
    

class Wishlist(models.Model):
    userid=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    movieid=models.ForeignKey(Movie,on_delete=models.CASCADE,null=True)
    qty=models.PositiveIntegerField(default=0)


