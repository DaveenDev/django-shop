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
    
class Customer(models.Model):
    # id -auto
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField()
    address1 = models.CharField(max_length=150, null=False)
    address2 = models.CharField(max_length=150, null=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code= models.CharField(max_length=20)
    
class Order(models.Model):
    # id -auto
    order_date = models.DateField()
    order_total = models.FloatField()
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT,related_query_name="orders")

class OrderItems(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_query_name="order_items")
    item_id = models.IntegerField()
    item_name = models.CharField(max_length=200)
    item_price = models.FloatField()
    item_amount = models.FloatField()