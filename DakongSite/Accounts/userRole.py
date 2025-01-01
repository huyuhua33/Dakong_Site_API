from django.db import models

class RoleChoices(models.TextChoices):
    GUEST = 'guest', 'Guest'
    USER = 'user', 'User'
    ADMIN = 'admin', 'Admin'

