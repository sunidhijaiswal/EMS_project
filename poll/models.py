from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


# Create your models here.
class Question(models.Model):
    tittle = models.TextField(null=True,blank=None)
    status = models.CharField(max_length=10)
    created_by = models.ForeignKey(User,on_delete = models.CASCADE,null=True,blank = None)
    start_date = models.DateTimeField(null=True,blank=None)
    end_date = models.DateTimeField(null=True,blank=None)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.tittle

    @property
    def choices(self):
        return self.choice_set.all()


class Choice(models.Model):
    question = models.ForeignKey('poll.Question',on_delete = models.CASCADE)
    text = models.TextField(null=True,blank=None)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

    @property
    def votes(self):
        return self.answer_set.count()



class Answer(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.first_name + '-' + self.choice.text
