from django.db import models

class Item(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='items/')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    URL = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title

