from django.db import models

class Notification(models.Model):
    id = models.CharField(max_length=255, primary_key=True)
    user_id = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    desc = models.TextField()
    data = models.TextField()
    image = models.ImageField(upload_to='notifications/')
    date = models.DateTimeField(auto_now_add=True)
    type = models.CharField(max_length=255)

    def __str__(self):
        return f"Уведомление {self.title} для пользователя {self.user_id}"
    
    class Meta:
        verbose_name = ""
        verbose_name_plural = "Настройки уведомдений"
