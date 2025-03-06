from django.db import models

# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=200)  # Course title
    description = models.TextField()  # Course description
    price = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)  # Course price
    date_created = models.DateTimeField(auto_now_add=True)  # Auto timestamp when created

    def __str__(self):
        return self.title
    