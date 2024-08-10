from django.db import models
from apps.warehouse.models import Warehouse

class Product(models.Model):
    id = models.CharField(max_length=255, primary_key=True)
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE, related_name='products')
    num_amount = models.IntegerField(default=0)
    user_id = models.CharField(max_length=255)
    image = models.ImageField(upload_to='products/')
    code = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    amount_type = models.CharField(max_length=255)
    cost_price = models.DecimalField(max_digits=10, decimal_places=2)
    cost_currency = models.CharField(max_length=10)
    sell_price = models.DecimalField(max_digits=10, decimal_places=2)
    sell_currency = models.CharField(max_length=10)
    expiration_date = models.DateField()
    deliver_date = models.DateField()

    def __str__(self):
        return f"Продукт {self.name} на складе {self.warehouse.name}"
    
    class Meta:
        verbose_name = ""
        verbose_name_plural = "Настройки продуктов"
