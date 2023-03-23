from django.db import models


# Create your models here.
class UniversityCampus(models.Model):
    Campus_Name = models.CharField(max_length=55, default="", blank=True, null=False)
    State = models.CharField(max_length=2, default="", blank=True, null=False)
    Campus_ID = models.IntegerField(default="", blank=True, null=False)


    def __str__(self):
        display_campus = '{0.Campus_Name}: {0.State}'
        return display_campus.format(self)

    class Meta:
        verbose_name_plural = "University Campus"

