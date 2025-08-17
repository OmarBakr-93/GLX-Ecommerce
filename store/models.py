from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=250, db_index=True)
    slug = models.SlugField(max_length=250, unique=True)
    
    class Meta:
        ordering = ('name',)
        verbose_name = 'التصنيفات'

    def __str__(self):
        return self.name
      
      
class Product(models.Model):
    category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=250, db_index=True)
    brand = models.SlugField(max_length=250, db_index=True)
    description = models.TextField(blank=True, max_length=5000)
    slug = models.SlugField(max_length=250)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='images/', blank=True)

    
    class Meta:
        verbose_name = 'المنتجات'

    def __str__(self):
        return self.title