from django.db import models
from django.contrib.auth.models import User
 
class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50, null=True) #    If True, Django will store empty values as NULL in the database. Default is False.
    city = models.CharField(max_length=60)
    state_province = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    website = models.URLField()

    def __str__(self):
        return self.name
    
    class Meta:
        db_table='publisher'
        verbose_name_plural='publishers'
 
class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    email = models.EmailField()

    def __str__(self):
        return self.first_name
    
    class Meta:
        db_table='author'
        verbose_name_plural='authors'
 
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher, on_delete=models.DO_NOTHING )
    publication_date = models.DateField()

    def __str__(self):
        return self.title
    
    class Meta:
        db_table='book'
        verbose_name_plural='books'