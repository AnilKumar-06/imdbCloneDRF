from django.db import models
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
# Register your models here.

class StreamPlateform(models.Model):

    name = models.CharField(max_length=50)
    about = models.CharField(max_length=100)
    website = models.URLField(max_length=100)

    def __str__(self):
        return self.name

class WatchList(models.Model):
    
    title = models.CharField(max_length=50)
    storyline = models.CharField(max_length=200)
    avg_rating = models.FloatField(default=0)
    number_rating = models.IntegerField(default=0)
    platform = models.ForeignKey(StreamPlateform, on_delete=models.CASCADE, related_name='watch_list')
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class Review(models.Model):
    
    rating = models.PositiveBigIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    review_user = models.ForeignKey(User, on_delete=models.CASCADE)
    desc = models.CharField(max_length=100)
    watchlist = models.ForeignKey(WatchList, on_delete=models.CASCADE, related_name='reviews')
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    def __str__(self):
        string = str(self.rating) + " " + str(self.watchlist.title)
        return string
    