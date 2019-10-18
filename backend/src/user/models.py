from django.db import models
from django.contrib.auth import get_user_model
from donor.models import Hall, Department
from django.db.models.signals import post_save

class Profile(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    full_name = models.CharField(max_length=50)
    dept = models.ForeignKey(Department, on_delete=models.CASCADE)
    batch = models.CharField(max_length=2)
    hall = models.ForeignKey(Hall, on_delete=models.CASCADE)
    isAdmin = models.BooleanField(default=False)
    isApproved = models.BooleanField(default=False)

# def create_profile(sender, **kwargs):
#     print(kwargs)
#     if kwargs['created']:
#         profile = Profile.objects.create(user=kwargs['instance'])

# post_save.connect(create_profile, sender=get_user_model())