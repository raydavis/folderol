from django.db import models
from django.db.models.signals import post_init
from django.dispatch import receiver
from campus_models import CampusPersonAttributes

class CalCentralUser(models.Model):
    uid = models.CharField(max_length=40)
    custom_preferred_name = models.CharField(max_length=400, db_column='preferred_name')
    campus_attributes = None

    def __unicode__(self):
        return str(vars(self))

    @property
    def preferred_name(self):
        print 'custom_preferred_name=', self.custom_preferred_name
        if not self.campus_attributes:
            self.campus_attributes = CampusPersonAttributes.objects.get(pk=self.uid)
        print 'campus_attributes=', self.campus_attributes
        val = self.custom_preferred_name or self.campus_attributes.person_name
        return val
    @preferred_name.setter
    def preferred_name(self, value):
        self.custom_preferred_name = value
