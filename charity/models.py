from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Institution(models.Model):
    CHOICES = (
        ('fundacja', 'fundacja'),
        ('organizacja pozarządowa', 'organizacja pozarządowa'),
        ('zbiórka lokalna', 'zbiórka lokalna')
    )
    name = models.CharField(max_length=255)
    description = models.TextField()
    type = models.CharField(max_length=255, choices=CHOICES, default='fundacja')
    category = models.ManyToManyField(Category)

    def __str__(self):
        return self.name


class Donation(models.Model):
    quantity = models.PositiveSmallIntegerField()
    categories = models.ManyToManyField(Category)
    institution = models.ForeignKey(Institution, on_delete=models.DO_NOTHING)
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=9)
    city = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=6)
    pick_up_date = models.DateField()
    pick_up_time = models.TimeField()
    pick_up_comment = models.TextField()
    user = models.ForeignKey(User, null=True, default=None, on_delete=models.DO_NOTHING)
    is_taken = models.BooleanField(default=False)
