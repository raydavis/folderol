from tastypie import fields, utils
from tastypie.authorization import Authorization
from tastypie.resources import ModelResource
from cc_app.models import CalCentralUser

class UserResource(ModelResource):
    preferred_name = fields.CharField(attribute="preferred_name", readonly=True)
    class Meta:
        queryset = CalCentralUser.objects.all()
        resource_name = 'user'
        authorization= Authorization()
