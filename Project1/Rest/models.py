from django.db import models


class Category(models.Model):
    name=models.CharField(max_length=100,db_index=True)
    slug=models.SlugField(max_length=100,db_index=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category,
                                 related_name='products',
                                 on_delete=models.CASCADE)
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100 , db_index=True)
    description = models.TextField(blank=True,db_index=True)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    # image = models.ImageField()

    # class Meta:
    #     ordering = ('name',)

    def __str__(self):
        return self.name
        
    
