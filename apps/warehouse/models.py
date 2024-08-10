from django.db import models

class Permission(models.Model):
    employee_id = models.CharField(max_length=255, unique=True)
    add = models.BooleanField(default=False)
    sell = models.BooleanField(default=False)
    edit = models.BooleanField(default=False)
    see_cost_price = models.BooleanField(default=False)
    see_sell_price = models.BooleanField(default=False)
    see_amount = models.BooleanField(default=False)

    def __str__(self):
        return f"Разрешения для сотрудника с ID: {self.employee_id}"
    
    class Meta:
        verbose_name = ""
        verbose_name_plural = "Настройки доступа сотрудникам" 

class Warehouse(models.Model):
    id = models.CharField(max_length=255, primary_key=True)
    name = models.CharField(max_length=255)
    num_amount = models.IntegerField(default=0)
    created_date = models.DateTimeField(auto_now_add=True)
    access = models.ManyToManyField(Permission, related_name="warehouses")

    def __str__(self):
        return f"Склад {self.name} ({self.id})"
    
    class Meta:
        verbose_name = ""
        verbose_name_plural = "Настройки склада"
