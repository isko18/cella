from django.db import models
from apps.warehouse.models import Warehouse

class HistoryProduct(models.Model):
    id = models.CharField(max_length=255, primary_key=True)
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE)
    amount = models.IntegerField(default=0)
    amount_type = models.CharField(max_length=255)
    code = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    sold_price = models.DecimalField(max_digits=10, decimal_places=2)
    sold_currency = models.CharField(max_length=10)

    def __str__(self):
        return f"История продукта {self.name} со склада {self.warehouse.name}"
    
    class Meta:
        verbose_name = ""
        verbose_name_plural = "Настрйки истории продукта"

class History(models.Model):
    id = models.CharField(max_length=255, primary_key=True)
    products = models.ManyToManyField(HistoryProduct, related_name='histories')
    user_id = models.CharField(max_length=255)
    buyer_name = models.CharField(max_length=255)
    debt = models.DecimalField(max_digits=10, decimal_places=2)
    debt_return_date = models.DateField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"История для пользователя {self.user_id}"
    
    class Meta:
        verbose_name = ""
        verbose_name_plural = "Настройки истории пользователя"
