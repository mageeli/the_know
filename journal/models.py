from django.db import models

from goals.models import Goal, Action
from django.contrib.auth.models import User


class Entry(models.Model):
    goal = models.ForeignKey(Goal, on_delete=models.CASCADE, null=True)
    progress = models.TextField()
    date_of_entry = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Entries'
        ordering = ['-date_of_entry', ]

    def __str__(self):
        return '{} {}'.format(self.goal, self.date_of_entry)
