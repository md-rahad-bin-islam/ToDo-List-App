from django.db import models

# Create your models here.
class Todo(models.Model):
    name = models.CharField(max_length=500)
    des = models.CharField(max_length=500)
    email = models.CharField(max_length=500, blank=True, default='abd@gmail.com')
    complete_in = models.IntegerField()
    progress = models.CharField(max_length=800, default="Started", blank=True)

    def __str__(self):
        return self.name