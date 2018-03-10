from django.db import models
from django.contrib.auth.models import User


class QuestionManager(models.Manager):
    def new(self):
        return self.order_by('-added_at')
    def popular(self):
        return self.order_by('-raiting')


class Question(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    rating = models.DecimalField(max_digits=4, decimal_places=2)
    author = models.OneToOneField(User,on_delete=models.SET_DEFAULT, default="Admin")
    likes = models.ManyToManyField(User, related_name='likes')

    objects = QuestionManager()


class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    author = models.OneToOneField(User, on_delete=models.SET_DEFAULT, default="Admin")