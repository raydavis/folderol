from django.db import models

class CalCentralUser(models.Model):
    uid = models.CharField(max_length=40)
    preferred_name = models.CharField(max_length=400)
    def __unicode__(self):
        return str(vars(self))
