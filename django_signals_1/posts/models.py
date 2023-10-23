from django.db import models
from django.db.models.signals import post_save, pre_save, post_delete


class Post(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


def save_post(sender, instance, **kwargs):
    print("something")

def after_delete_post(sender, instance, **kwargs):
    print('you deleted something')

post_save.connect(save_post, sender=Post)
pre_save.connect(save_post, sender=Post)
post_delete.connect(after_delete_post, sender=Post)



"""
>>> from posts.models import Post
>>> p = Post.objects.create(title='first title')
something
>>> p
<Post: first title>
>>> p2 = Post()
>>> p2.title='second title'
>>> p2.save()
something
>>> 

>>> from posts.models import Post
>>> p = Post.objects.first()
>>> p
<Post: first title>
>>> p.delete()
you deleted something
(1, {'posts.Post': 1})
>>> 


    
"""