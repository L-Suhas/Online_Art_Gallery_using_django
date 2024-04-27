from django.db import models
from django.template.context_processors import request


# Create your models here.
class category(models.Model):
    title=models.CharField(max_length=100)
    image=models.ImageField(upload_to="cat_imgs/")

    def __str__(self):
        return self.title

# Products

class product(models.Model):
    title=models.CharField(max_length=200)
    image = models.ImageField(upload_to="product_imgs/")
    slug=models.CharField(max_length=400)
    detail=models.TextField()
    description=models.TextField()
    price=models.PositiveIntegerField()
    status=models.BooleanField(default=True)

    def __str__(self):
        return self.title

