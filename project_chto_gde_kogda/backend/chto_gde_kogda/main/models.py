from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=100)
    def __str__(self):
        return self.title

class MetroStation(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Thing(models.Model):
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='things')
    metro = models.ForeignKey(MetroStation, on_delete=models.PROTECT, related_name='things')
    address = models.CharField(max_length=250)
    description = models.TextField()

    thing_photo = models.ImageField(upload_to='photos/%y/%m/%d')
    place_photo = models.ImageField(upload_to='photos/%y/%m/%d')
    additional_photo = models.ImageField(upload_to='photos/%y/%m/%d')

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.category} - {self.description[:50]}'
