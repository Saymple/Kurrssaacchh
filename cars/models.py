from django.db import models
from django.conf import settings


class Car(models.Model):

    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    brand = models.CharField(
        max_length=100
    )

    model = models.CharField(
        max_length=100
    )

    year = models.PositiveIntegerField()

    mileage = models.PositiveIntegerField()

    price = models.PositiveBigIntegerField()

    description = models.TextField()

    image = models.ImageField(
        upload_to='cars/'
    )

    is_active = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f'{self.brand} {self.model}'