"""importes para criação de modelos do aplicativo users."""
from django.db import models
from django.contrib.auth.models import User


class UserProfileExample(models.Model):
    """modelo de exemplo para criar um perfil de usuário"""
    phone_number = models.CharField(max_length=12)
    address = models.CharField(max_length=150)
    birth_date = models.DateField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        """Meta class para o modelo UserProfileExample."""
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"
