# # Account App
# # Account/models.py (Extending the User Model)
# from django.contrib.auth.models import AbstractUser
# from django.db import models
# import logging

# logger = logging.getLogger(__name__)

# class CustomUser(AbstractUser):
#     phone_number = models.CharField(max_length=15, blank=True, null=True)
#     address = models.TextField(blank=True, null=True)

#     def __str__(self):
#         return self.username

# logger.info("CustomUser model loaded successfully.")
from django.contrib.auth.models import AbstractUser
from django.db import models
import logging

logger = logging.getLogger(__name__)

class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)

    # Add related_name to avoid reverse accessor clash
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_groups',
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_user_permissions',
        blank=True
    )

    def __str__(self):
        return self.username

logger.info("CustomUser model loaded successfully.")
