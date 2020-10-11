from django.db import models

# Create your models here.
class Todo(models.Model):
    task = models.CharField(max_length=100)
    description = models.TextField(max_length=200)
    task_time = models.DateTimeField()
    is_completed = models.BooleanField(default=False)
    is_important = models.BooleanField()

    def get_absolute_url(self):
        return "{pk}/".format(pk=self.id)

    def __str__(self):
        return self.task
