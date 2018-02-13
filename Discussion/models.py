from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
       Token.objects.create(user=instance)


class Discussion(models.Model):
    discussion_type = (
			('article', 'Article'),
			('blog', 'Blog'), 
			('question', 'Question'),
            ('post','Post')
		)
        # 'Article', 'Question', 'Post', 'Blog'

    added_by = models.ForeignKey(User, related_name='discussions',default=1)
    # added_by = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    modified_date = models.DateTimeField(blank=True, null=True)
    discussion_type = models.CharField(choices=discussion_type, max_length=10, null=True, blank=True)
	# is_active = models.BooleanField(default=True)
    image = models.ImageField(upload_to='post_images/', null=True, blank=True)


    def __str__(self):
		return self.title


class Comment(models.Model):
    discussion = models.ForeignKey(Discussion, related_name='discussion_comments')
    text = models.TextField()
    added_by = models.ForeignKey(User, related_name='Comments',default=1)
    created_date = models.DateTimeField(default=timezone.now)
    modified_date = models.DateTimeField(blank=True, null=True)
    
    def __str__(self):
		return self.text
