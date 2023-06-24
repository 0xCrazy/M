from django.db import models
from django.contrib.auth.models import UserManager

# Create your models here.

class StationName(models.Model):
    pass

class EmployeeDataManager(UserManager):
    pass

class ClientData(models.Model):
    pass

class MaternityData(models.Model):
    pass

class MenstruationData(models.Model):
    pass

class SpecialTestData(models.Model):
    pass

class ReportsData(models.Model):
    pass


class Notification(models.Model):
    pass


