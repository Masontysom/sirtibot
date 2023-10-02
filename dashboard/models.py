from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class MCQ(models.Model):
    text = models.TextField()
    question = models.CharField(max_length=200)
    choices = models.JSONField()
    correct_choice = models.IntegerField()
class Meta:
        app_label = 'dashboard'

 
# Create your models here.
class QuesModel(models.Model):
    question = models.CharField(max_length=200,null=True)
    op1 = models.CharField(max_length=200,null=True)
    op2 = models.CharField(max_length=200,null=True)
    op3 = models.CharField(max_length=200,null=True)
    op4 = models.CharField(max_length=200,null=True)
    ans = models.CharField(max_length=200,null=True)
    
    def __str__(self):
        return self.question
    
