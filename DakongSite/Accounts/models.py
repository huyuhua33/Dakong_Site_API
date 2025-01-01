from django.db import models
from django.contrib.auth.models import AbstractUser
from .userRole import RoleChoices
import uuid



# Helper function to generate prefixed UUID
def generate_prefixed_uuid():
    return f"AC{uuid.uuid4()}"

# Models
class RoleHierarchy(models.Model):
    role = models.CharField(
        max_length=50,
        choices=RoleChoices.choices,
        default=RoleChoices.GUEST,
        unique=True
    )
    level = models.PositiveIntegerField(unique=True)

    class Meta:
        ordering = ['level']

    def save(self, *args, **kwargs):
        """Ensure levels are incrementally assigned"""
        if not RoleHierarchy.objects.filter(level=self.level).exists():
            super().save(*args, **kwargs)
        else:
            raise ValueError("Level values must be unique and incrementally assigned.")

    def __str__(self):
        return f"{self.role} (Level {self.level})"

class User(AbstractUser):
    id = models.CharField(
        max_length=40,
        primary_key=True,
        default=generate_prefixed_uuid,
        editable=False
    )
    roles = models.ManyToManyField(RoleHierarchy, blank=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.username
    class Meta:
        db_table = 'Accounts_user'

    def has_permission_level(self, required_role):
        """Check hierarchical role permissions"""
        return any(role.level >= required_role.level for role in self.roles.all())

