from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

# Create your models here.
class Student(AbstractBaseUser):
    username = models.CharField(
        max_length=255,
        unique=True,
        blank=False,
        null=False
    )
    first_name = models.CharField(max_length=255)
    mid_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='media/')

    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    students = StudentManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['username']

    def get_full_name(self):
        return '{0} {1} {2}'.format(
            self.last_name,
            self.first_name,
            self.mid_name
        )

    def get_short_name(self):
        return '{0} {1}'.format(
            self.last_name,
            self.first_name,
        )

    def get_personal_number(self):
        return self.username

    def get_username(self):
        return get_personal_number()

    def __str__(self):
        return get_full_name()

    def has_pem(self, perm, obj=None):
        return self.is_admin and self.is_staff

    def has_module_perms(self, app_label):
        return self.is_admin or self.is_staff

    @property
    def is_staff(self):
        return self.is_staff or self.is_admin

    @property
    def is_admin(self):
        return self.is_admin

    @property
    def is_active(self):
        return self.is_active


class StudentManager(BaseUserManager):
    pass
