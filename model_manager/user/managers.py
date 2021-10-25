from django.db import models

class CustomManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().all().order_by('age')

class Customage(models.Manager):
    def get_Detail_age_range(self,r1,r2):
        return super().get_queryset().filter(age__range=(r1,r2))
