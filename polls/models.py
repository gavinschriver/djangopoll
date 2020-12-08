import datetime
from django.db import models
from django.utils import timezone

# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date WE DANG published')
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text

class Place(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=80)
    def __str__(self):
        return f"{self.name} the place"

class Restaurant(models.Model):
    place = models.OneToOneField(
        Place, on_delete=models.CASCADE,
        primary_key=True
    )
    def __str__(self):
        return f"{self.name} the restaurant"


class Waiter(models.Model):
    employed_at = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        pass


