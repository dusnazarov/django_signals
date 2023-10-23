from django.db import models
from django.utils.text import slugify
from django.conf import settings
from django.utils import timezone
# django signals import
from django.dispatch import receiver
from django.db.models.signals import post_save, pre_save, post_delete
1


User = settings.AUTH_USER_MODEL


class BlogPost(models.Model):
    title = models.CharField(max_length=120)
    slug = models.SlugField(blank=True, null=True)
    liked = models.ManyToManyField(User, blank=True)
    notify_users = models.BooleanField(default=False)
    notify_users_timestap = models.DateTimeField(blank=True, null=True, auto_now_add=False)
    active = models.BooleanField(default=True)


# # ///////////////////////
# @receiver(post_save, sender=BlogPost)
# def blog_post_post_save(sender, instance, created, *args, **kwargs):
#     if not instance.slug:
#         instance.slug = slugify(instance.title)
#         instance.save()

# # ///////////////////////
# @receiver(pre_save, sender=BlogPost)
# def blog_post_post_save(sender, instance, *args, **kwargs):
#     if not instance.slug:
#         instance.slug = slugify(instance.title)  

# # # ///////////////////////
# @receiver(pre_save, sender=BlogPost)
# def blog_post_pre_save(sender, instance, *args, **kwargs):
#     if not instance.slug:
#         instance.slug = slugify(instance.title) 

#     if instance.id and instance.notify_users:
#         print("notify users")
#         instance.notify_users=False

# # # ///////////////////////
# @receiver(pre_save, sender=BlogPost)
# def blog_post_pre_save(sender, instance, *args, **kwargs):
#     if not instance.slug:
#         instance.slug = slugify(instance.title) 

#     if instance.id and instance.notify_users:
#         print("notify users")
#         instance.notify_users=False
#         instance.notify_users_timestap = timezone.now()

# # ///////////////////////
@receiver(pre_save, sender=BlogPost)
def blog_post_post_save(sender, instance, *args, **kwargs):
    
    if instance.notify_users:
        print("notify users")
        instance.notify_users=False
        instance.notify_users_timestap = timezone.now()
        instance.save()






    






