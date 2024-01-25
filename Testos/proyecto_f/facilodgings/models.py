from django.db import models

class Facilodgings(models.Model):
    lodging = models.ForeignKey('lodgings.Lodging', on_delete=models.DO_NOTHING)
    facilitie = models.ForeignKey('facilities.Facilitie', on_delete=models.DO_NOTHING)
    status = models.BooleanField(default=True)
   
    def __str__(self):
        return self.lodging
