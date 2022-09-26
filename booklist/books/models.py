from django.conf import settings
from django.urls import reverse

from django.db import models

STATUS_CHOICES = (
    ('reading', 'Reading'),
    ('finished', 'Finished'),
)

class Book(models.Model):
    def get_absolute_url(self):
     return reverse("book_detail", kwargs={
        "pk": self.id
    })
    title = models.CharField(max_length=150)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        related_name="books"
    )
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES
    )

def __str__(self):
    return self.title



# Create your models here.
