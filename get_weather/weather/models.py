from django.db import models


class CitySearch(models.Model):
    city_name = models.CharField(max_length=100, db_index=True)
    search_count = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.city_name}: {self.search_count}"
