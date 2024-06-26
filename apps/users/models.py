from typing import Iterable
from django.db import models
from django.utils.crypto import get_random_string

from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    phone = models.CharField(
        max_length = 255,
        verbose_name = 'Номер телефона'
    )
    age = models.IntegerField(
        default=0,
        verbose_name = 'Возраст',
    )
    balance = models.PositiveIntegerField(
        default=0,
        verbose_name = 'Баланс',
        blank=True, null=True
    )
    wallet_address = models.DateTimeField(
        max_length = 255,
        unique=True, blank=True, null=True,
        verbose_name = 'ID кошелька' 
    )
    created_at = models.DateTimeField(
        auto_now_add = True,
        verbose_name = 'Дата регистрации' 
    )
    
    def save(self, *args, **kwargs):
        if not self.wallet_address:
            unique_address_genereted = False
            while not unique_address_genereted:
                wallet_address = get_random_string(length=12)
                if not User.objects.filter(wallet_address=wallet_address).exists():
                    unique_address_genereted = True
                    self.wallet_address = wallet_address
                super().save(*args, **kwargs)
    
    def __str__(self):
        return self.username
    
    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        
        

class HistoryTransfer(models.Model):
    from_user = models.ForeignKey(
        User, related_name = 'transfer_sent',
        on_delete = models.CASCADE,
        verbose_name = 'От пользователя'
    )
    to_user = models.ForeignKey(
        User, related_name = 'transfer_received',
        on_delete = models.CASCADE,
        verbose_name = 'К пользователю'
    )
    is_comleted = models.BooleanField(
        default = False,
        verbose_name = 'Статус выполнения'
    )
    amount = models.PositiveIntegerField(
        verbose_name='Сумма', 
        default=0
    )
    created_at = models.DateTimeField(
        auto_now_add=True, 
        verbose_name='Дата создания'
    )

    def __str__(self):
        return f"{self.from_user} отправлено {self.to_user}"
    
    class Meta:
        verbose_name = 'Перевод'
        verbose_name_plural = 'Переводы'
        