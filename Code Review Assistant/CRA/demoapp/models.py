from django.db import models

# Create your models here.


class signup(models.Model):
    D_id = models.IntegerField(primary_key=True)
    password = models.CharField(max_length=20)
    email = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return str(self.D_id)


class submissions(models.Model):
    sub_id = models.IntegerField(primary_key=True)
    D_id = models.IntegerField()
    code = models.CharField(max_length=1000000)
    gemini_output = models.TextField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
