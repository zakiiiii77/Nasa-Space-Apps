from django.db import models

# Create your models here.
class Data(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.PositiveIntegerField(default=0)

    class Meta:
      verbose_name_plural = "nasaa"

    def __str__(self):
        return self.first_name