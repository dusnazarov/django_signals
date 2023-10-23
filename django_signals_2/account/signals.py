from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from .models import Profile



@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):  

    if created:
        Profile.objects.create(user=instance)
        print("Profilo created!")

# post_save.connect(create_profile, sender=User)

@receiver(post_save, sender=User)
def update_profile(sender, instance, created, **kwargs):

    if created == False:
        instance.profile.save()
        print("Profile updated!")

# post_save.connect(update_profile, sender=User)


""" 
in the app.py, we added  this 

( 
from django.apps import AppConfig


class AccountConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'account'

    def ready(self):
        import account.signals
)
"""
