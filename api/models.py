from django.db import models


class Item(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
    item_number = models.IntegerField(),
    name = models.CharField(max_length=50, null=False)
    category = models.CharField(max_length=15, null=False)
    type = models.CharField(max_length=30)
    group = models.CharField(max_length=30)
    standard = models.FloatField()
    standard_hc = models.FloatField()
    current = models.FloatField()
    current_hc = models.FloatField()

    def __str__(self):
        return f'{self.name} ({self.category})'
