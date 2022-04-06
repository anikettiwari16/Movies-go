import os
from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.
def path_and_rename(instance, filename):
    upload_to = 'Images/'
    ext = filename.split('.')[-1]    
    filename = 'Movie_Images/{}.{}'.format(instance.slug, ext)
    return os.path.join(upload_to, filename)
    

class Movie(models.Model):
    movie_type = [
        ('Action','Action'),
        ('Comedy','Comedy'),
        ('Drama','Drama'),
        ('Fantasy','Fantasy'),
        ('Mystery','Mystery'),
        ('Romance','Romance'),
        ('Thriller','Thriller'),
    ]
    name = models.CharField(max_length=200,blank=True)
    slug = models.SlugField(null=True,blank=True)
    movie_duration = models.DurationField(null=True, blank=True)
    price = models.IntegerField(blank=True)    
    movie_pic = models.ImageField(upload_to=path_and_rename,verbose_name='Movie Picture',blank=True)
    description = models.TextField(blank=True)
    date_created = models.DateField(blank=True,auto_now=True)
    genres = models.CharField(max_length=10,choices=movie_type,blank=True)
    def __str__(self):
        return self.name
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

#City 
class City(models.Model):    
    name = models.CharField(max_length=100, blank=True)
    slug = models.SlugField(null=True,blank=True)   
    def __str__(self):
        return self.name
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

#Theater
class Theater(models.Model):
    name = models.CharField(max_length=100,blank=True)
    slug = models.SlugField(null=True,blank=True)
    city = models.ForeignKey(City,on_delete=models.DO_NOTHING)
    streetNo = models.CharField(max_length=100, blank=True) 
    landmark = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

#Seat And Booking Logic

class Booking(models.Model):
    time_choice = [
        ('09:00:00 - 12:00:00','09:00:00 - 12:00:00'),
        ('12:00:00 - 03:00:00','12:00:00 - 03:00:00'),
        ('03:00:00 - 06:00:00','03:00:00 - 06:00:00'),
        ('06:00:00 - 09:00:00','06:00:00 - 09:00:00'),
    ]
    movie = models.ForeignKey(Movie,on_delete=models.DO_NOTHING,null=True )
    theater = models.ForeignKey(Theater,on_delete=models.DO_NOTHING,null=True)
    time = models.CharField(choices=time_choice,null=True,max_length=30)
    seat = models.CharField(null=True,max_length=100)
    def __str__(self):
        return self.movie.name+" - "+str(self.theater.name)+" - "+str(self.time)+" - "+str(self.seat)