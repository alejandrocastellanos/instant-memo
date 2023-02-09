from datetime import date

from django.db import models


class Notes(models.Model):

    title = models.CharField(max_length=200)
    text_note = models.CharField(max_length=500)
    color_note = models.CharField(max_length=500, null=True)
    create_date = models.DateTimeField("create date", default=date.today)
    dead_line = models.DateTimeField("Deadline", null=True)

    def __str__(self):
        return self.title
