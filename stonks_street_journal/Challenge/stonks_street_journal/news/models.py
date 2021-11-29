from django.db import models
from django.forms import ModelForm


# Create your models here.
class Subscriber(models.Model):
    username = models.SlugField(unique=True)
    password = models.CharField(max_length=255)
    pensi = models.IntegerField()
    email = models.EmailField()
    credit_card = models.CharField(max_length=19)
    signup_date = models.DateField(auto_now=True)

class Article(models.Model):
    publish_time = models.DateTimeField(auto_now=True)
    headline = models.CharField(max_length=150)
    text = models.CharField(max_length=1024)


class SubscriberForm(ModelForm):
    class Meta:
        model = Subscriber
        exclude = ["signup_date"]