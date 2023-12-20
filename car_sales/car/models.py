from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class brand(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, null=True, blank=True)

    def __str__(self):
        return self.name

class car(models.Model):
    image = models.ImageField(upload_to='car/media/uploads/',null=True,blank=True)
    car_name = models.CharField(max_length = 100)
    car_brand = models.ForeignKey(brand, on_delete=models.CASCADE)
    description = models.TextField()
    quantity = models.IntegerField()
    price = models.IntegerField()

    def __str__(self):
        return self.car_name
    
class buy_record(models.Model):
    buyer = models.ForeignKey(User, on_delete=models.CASCADE)
    car_bought = models.ForeignKey(car, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.buyer}-{self.car_bought}'
    
class comment(models.Model):
    cr = models.ForeignKey(car, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=50)
    email = models.EmailField()
    comment_area = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True) 
    
    def __str__(self):
        return f"Comments by {self.name}"