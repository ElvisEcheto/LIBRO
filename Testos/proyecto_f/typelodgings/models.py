from django.db import models

class Typelodging(models.Model):
    image = models.ImageField(upload_to='typelodging_images', null=True)
    name = models.CharField(max_length=255)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name