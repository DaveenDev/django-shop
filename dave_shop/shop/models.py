from django.db import models

# Create your models here.
class Category(models.Model):
    # id - auto
    category = models.CharField(max_length=150)
    
    def __str__(self):
        return self.category
    
    class Meta:
        verbose_name_plural = "Categories"

class Product(models.Model):
    title = models.CharField(max_length=200)
    price = models.FloatField(null=True, blank=True)
    discounted_price = models.FloatField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE,
                                 null=True)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to="product-images", null=True)
    slug = models.SlugField(null=True)
    
    class Meta:
        verbose_name_plural = "Products"
    