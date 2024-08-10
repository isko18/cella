from django.db import models

class Employee(models.Model):
    id = models.CharField(max_length=255, primary_key=True)
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    photo = models.ImageField(upload_to='employees/')

    def __str__(self):
        return f"Сотрудник {self.name}"
    
    class Meta:
        verbose_name = ""
        verbose_name_plural = "Сотрудники"

class User(models.Model):
    id = models.CharField(max_length=255, primary_key=True)
    full_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='users')
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Пользователь {self.full_name}"
    
    class Meta:
        verbose_name = ""
        verbose_name_plural = "Пользователи"

