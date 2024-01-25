from django.db import models

class Lodging(models.Model):
    image = models.ImageField(upload_to='lodgings_images', null=True)
    price = models.IntegerField()
    capacity= models.IntegerField()
    typelodging = models.ForeignKey('typelodgings.Typelodging', on_delete=models.DO_NOTHING)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.image
