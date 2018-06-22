from django.db import models

# Create your models here.
class Stock(models.Model):
    stock_name = models.CharField(max_length = 200)
    stock_price = models.CharField(max_length = 200)
    stock_gain = models.CharField(max_length = 200)
    market_name = models.CharField(max_length = 200)
