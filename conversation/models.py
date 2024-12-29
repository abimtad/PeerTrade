from django.db import models
from item.models import Item
from django.contrib.auth.models import User

class Conversation(models.Model):
	item = models.ForeignKey(Item, related_name='conversations', on_delete=models.CASCADE)
	members = models.ManyToManyField(User, related_name='conversations')
	created_at = models.DateField(auto_now_add=True)
	updated_at = models.DateField(auto_now=True)


class ConvoMessage(models.Model):
	conversation = models.ForeignKey(Conversation, related_name='messages', on_delete=models.CASCADE)
	content = models.TextField()
	created_by = models.ForeignKey(User, related_name='messages', on_delete=models.CASCADE)
	created_at = models.DateTimeField(auto_now_add=True)
	
