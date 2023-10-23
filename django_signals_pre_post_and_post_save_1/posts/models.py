from django.db import models
from django.db.models.signals import post_save, pre_save, post_delete
from django.conf import settings
from django.dispatch import receiver


User = settings.AUTH_USER_MODEL


# //////////////////////////////
# def user_created_handler(*args, **kwargs):
#     print(args, kwargs)

# post_save.connect(user_created_handler, sender=User)

# //////////////////////////////
# @receiver(post_save, sender=User)
# def user_created_handler(*args, **kwargs):
#     print(args, kwargs)

# //////////////////////////////
# @receiver(post_save, sender=User)
# def user_created_handler(sender, instance, created, *args, **kwargs):
#     if created:
#         print('Send email to ', instance.username)
#     else:
#         print(instance.username, "was just saved")


# # //////////////////////////////
# @receiver(pre_save, sender=User)
# def user_pre_save_receiver(sender, instance,  *args, **kwargs):

#     """
#     before saved in the database

#     """     
#     print(instance.username, instance.id)
    

# @receiver(post_save, sender=User)
# def user_post_save_receiver(sender, instance, created, *args, **kwargs):
#     """
#     after saved in the database

#     """    

#     if created:
#         print('Send email to ', instance.username)
#     else:
#         print(instance.username, "was just saved")


# //////////////////////////////
# @receiver(pre_save, sender=User)
# def user_pre_save_receiver(sender, instance,  *args, **kwargs):

#     """
#     before saved in the database

#     """     
#     print(instance.username, instance.id)
    

# @receiver(post_save, sender=User)
# def user_post_save_receiver(sender, instance, created, *args, **kwargs):
#     """
#     after saved in the database

#     """    

#     if created:
#         print('Send email to ', instance.username)
#     else:
#         print(instance.username, "was just saved")


# //////////////////////////////
# @receiver(pre_save, sender=User)
# def user_pre_save_receiver(sender, instance,  *args, **kwargs):

#     """
#     before saved in the database

#     """     
#     print(instance.username, instance.id)
    

@receiver(post_save, sender=User)
def user_post_save_receiver(sender, instance, created, *args, **kwargs):
    """
    after saved in the database

    """    

    if created:
        print('Send email to ', instance.username)
        instance.save()
    else:
        print(instance.username, "was just saved")





    






