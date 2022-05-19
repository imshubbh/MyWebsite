from email.policy import default
import uuid
from django.db import models


class UrlShortner(models.Model):
    MainUrl = models.URLField(max_length=200, null=True)
    uuid = models.CharField(unique=True, max_length=15)
    Views = models.IntegerField(default=0)
    Active_Url = models.BooleanField(default=False, null=True)
    Paid = models.BooleanField(default=False)

    class Meta:
        ordering = ['-Views','-Paid']

    def clean(self):
        self.uuid = self.uuid.lower()


    def __str__(self):
         return self.MainUrl