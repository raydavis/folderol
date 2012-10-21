from tastypie.authorization import Authorization
from tastypie.resources import ModelResource
from cc_app.models import CalCentralUser

class UserResource(ModelResource):
    class Meta:
        queryset = CalCentralUser.objects.all()
        resource_name = 'user'
        authorization= Authorization()
