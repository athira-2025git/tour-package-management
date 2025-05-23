from django.db import models
from django.contrib.auth.models import User

class TourPackage(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.CharField(max_length=100)
    image = models.ImageField(upload_to='package_images/')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    expiry_date = models.DateField()
    approved = models.BooleanField(default=False)

    def __str__(self):
        return self.title
