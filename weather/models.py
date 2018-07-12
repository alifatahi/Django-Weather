from django.db import models


# Create your models here.

class City(models.Model):
    # Character with  max 25
    name = models.CharField(max_length=25)

    # Return String of Object
    def __str__(self):  # show the actual city name on the dashboard
        return self.name

    class Meta:  # show the plural of city as cities instead of citys
        # Declare name of table to be cities
        verbose_name_plural = 'cities'
