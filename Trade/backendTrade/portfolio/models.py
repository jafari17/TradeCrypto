from django.db import models

# Create your models here.

class Portfolio(models.Model):
    entry_date = models.DateField()
    type_position = models.BooleanField()
    currency = models.CharField(max_length=20)
    entry_price = models.IntegerField()
    dollar_value = models.IntegerField()
    coin_value = models.IntegerField()
    notes = models.CharField(max_length=500, default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.currency