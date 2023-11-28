from django.db import models

class student(models.Model):
    sid=models.IntegerField()
    sname=models.CharField(max_length=25)
    marks=models.IntegerField()
    class Meta:
        db_table="studentAWS"
