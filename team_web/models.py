from django.db import models

# Defines all the models for the application.

class Role(models.TextChoices):
    ADMIN = 'Admin', 'Admin'
    REGULAR = 'Regular', 'Regular Team Member'

# Defines TeamMember schema. Each team member has personal details and an assigned role.
class TeamMember(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100) 
    email = models.EmailField(max_length=100, unique=True)
    phone = models.CharField(max_length=20)
    role = models.CharField(max_length=20, choices=Role.choices)

    def __str__(self):
        return (f"{self.first_name} {self.last_name}")

