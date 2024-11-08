from django.contrib.auth import models as auth_models, get_user_model
from django.db import models

class AppUser(auth_models.AbstractUser, auth_models.PermissionsMixin):
    email = models.EmailField(unique=True, null=False, blank=False)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
