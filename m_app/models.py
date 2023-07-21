from typing import Any, Optional
from django.db import models
from django.contrib.auth.models import Group, Permission, AbstractBaseUser, PermissionsMixin, UserManager
from django.utils import timezone

# Create your models here.
MALE = 'MALE'
FEMALE = 'FEMALE'
GENDER = [
    (MALE, 'MALE'), (FEMALE, 'FEMALE')
]

PRIMARY = 'PRIMARY'
SECONDARY = 'SECONDARY'
HIGH_SCHOOL = 'HIGH SCHOOL'
UNIVERSITY = 'UNIVERSITY'
ILLITERACY = 'ILLITERACY'
EDUCATION_LEVEL = [
    (PRIMARY, 'PRIMARY'), (SECONDARY, 'SECONDARY'), (HIGH_SCHOOL, 'HIGH SCHOOL'), 
    (UNIVERSITY, 'UNIVERSITY'), (ILLITERACY, 'ILLITERACY')
]

NO_JOB = 'NO JOB'
ENTERPRENEUR = 'ENTERPRENEUR'
EMPLOYED = 'EMPLOYED'
FARMER = 'FARMER'
OCCUPATION = [
                (NO_JOB, 'NO JOB'), (ENTERPRENEUR, 'ENTERPRENEUR'), (EMPLOYED, 'EMPLOYED'), (FARMER, 'FARMER')
              ]

ARUSHA = 'Arusha' 
DARESSALAAM = 'Dar es Salaam' 
DODOMA = 'Dodoma' 
IRINGA = 'Iringa' 
KAGERA = 'Kagera'  
KIGOMA = 'Kigoma' 
KILIMANJARO = 'Kilimanjaro'
LINDI = 'Lindi' 
MANYARA = 'Manyara' 
MARA = 'Mara'
MBEYA = 'Mbeya' 
MOROGORO = 'Morogoro'
MTWARA = 'Mtwara'
MWANZA = 'Mwanza' 
PEMBA_NORTH = 'Pemba North (Wete)' 
PEMBA_SOUTH = 'Pemba South (Mkoani)' 
PWANI = 'Pwani (Kibaha)' 
RUKWA = 'Rukwa (Sumbawanga)' 
RUVUMA = 'Ruvuma (Songea)' 
SHINYANGA = 'Shinyanga' 
SINGIDA = 'Singida'
TABORA = 'Tabora'
TANGA = 'Tanga'  
ZANZIBAR_CENTRAL = 'Zanzibar Central/South (Koani)'
ZANZIBAR_NORTH = 'Zanzibar North (Mkokotoni)' 
ZANZIBAR_URBAN_WEST = 'Zanzibar Urban/West (Stone Town)'
RESIDENCE = [
    (ARUSHA, 'Arusha'), (DARESSALAAM, 'Dar es Salaam'), (DODOMA, 'Dodoma'), (IRINGA, 'Iringa'), 
(KAGERA, 'Kagera'), (KIGOMA, 'Kigoma'), (KILIMANJARO, 'Kilimanjaro'), (LINDI, 'Lindi'), (MANYARA, 'Manyara'), 
(MARA, 'Mara'), (MBEYA, 'Mbeya'), (MOROGORO, 'Morogoro'), (MTWARA, 'Mtwara'), (MWANZA, 'Mwanza'), 
(PEMBA_NORTH, 'Pemba North (Wete)'), (PEMBA_SOUTH, 'Pemba South (Mkoani)'), (PWANI, 'Pwani (Kibaha)'),
(RUKWA, 'Rukwa (Sumbawanga)'), (RUVUMA, 'Ruvuma (Songea)'), (SHINYANGA, 'Shinyanga'), (SINGIDA, 'Singida'), (TABORA, 'Tabora'),
(TANGA, 'Tanga'),  (ZANZIBAR_CENTRAL, 'Zanzibar Central/South (Koani)'), (ZANZIBAR_NORTH, 'Zanzibar North (Mkokotoni)'), 
(ZANZIBAR_URBAN_WEST, 'Zanzibar Urban/West (Stone Town)')

]



class StationName(models.Model):
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=250)
    registration_number = models.CharField(max_length=30)
    mobile_number = models.CharField(max_length=13)
    physical_address = models.CharField(max_length=100)
    
    class Meta:
        verbose_name = 'Station Name'
        verbose_name_plural = 'Station Names'

class EmployeeDataManager(UserManager):
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('Weka Barua Pepe Sahihi')
        
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user
    
    def create_user(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)
    

    def create_superuser(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(email, password, **extra_fields)
    



class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(blank=True, default='', unique=True)
    name = models.CharField(max_length=250, blank=True, default='')

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    date_joined = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(blank=True, null=True)

    groups = models.ManyToManyField(Group, related_name='m_app_users', blank=True, help_text='This user group belongs to', verbose_name='groups',)
    user_permissions = models.ManyToManyField(Permission, related_name='m_app_users', blank=True, help_text='specific permision for this user', verbose_name='user permisions')

    objects = EmployeeDataManager()

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    

    def get_full_name(self):
        return self.name
    

    def get_short_name(self):
        return self.name or self.email.split('@')[0]




class ClientData(models.Model):
    #---------clients--personal--details----------------------------
    full_name =''
    first_name = models.CharField(max_length=50,)
    middle_name = models.CharField(max_length=50,)
    last_name = models.CharField(max_length=50,)
    date_of_birth = models.DateField()
    age = ''
    gender = models.CharField(max_length=10, choices=GENDER, default='FEMALE')
    mobile_number = models.CharField(max_length=10, help_text='0762111127')
    education_level = models.CharField(max_length=30, choices=EDUCATION_LEVEL)
    curent_occupation = models.CharField(max_length=100, choices=OCCUPATION)
    residential_address = models.CharField(max_length=250, choices=RESIDENCE)

    class Meta:
        verbose_name = 'Client Data'
        verbose_name_plural = "Clients' Data"

    


class ClientsSpouseData(models.Model):
    #----------clients--spouse--detail---------------------------------------
    client = models.ForeignKey(ClientData, on_delete=models.SET_NULL, blank=True, null=True)
    full_name =''
    first_name = models.CharField(max_length=50,)
    middle_name = models.CharField(max_length=50,)
    last_name = models.CharField(max_length=50,)
    date_of_birth = models.DateField()
    age = ''
    gender = models.CharField(max_length=10, choices=GENDER, default='MALE')
    mobile_number = models.CharField(max_length=10, help_text='0762111127')
    education_level = models.CharField(max_length=30, choices=EDUCATION_LEVEL)
    curent_occupation = models.CharField(max_length=100, choices=OCCUPATION)
    residential_address = models.CharField(max_length=250, choices=RESIDENCE)

    class Meta:
        verbose_name = 'Client Spouse Data'
        verbose_name_plural = 'Client Spouses Data'

class MaternityData(models.Model):
    client  = models.ForeignKey(ClientData, on_delete=models.CASCADE, blank=True, null=True)
    birth_number = models.CharField(max_length=2,)
    number_of_time_given_birth = models.CharField(max_length=2)
    living_children = models.CharField(max_length=2)
    miscariages = models.CharField(max_length=2)
    year_of_miscariage = models.DateField(null=True)

    class Meta:
        verbose_name = 'Maternity Data'
        verbose_name_plural = 'Maternity Data'
    

class MenstruationData(models.Model):
    client = models.ForeignKey(ClientData, on_delete=models.CASCADE)
    period_length = models.PositiveIntegerField()
    cycle_length = models.PositiveIntegerField()
    start_date = models.DateField()
    end_date = models.DateField()

    class Meta:
        verbose_name = 'Menstruation Data'
        verbose_name_plural = 'Menstruation Data'
    

class SpecialTestData(models.Model):
    complete_blood_count = models.CharField(max_length=100)
    blood_type = models.CharField(max_length=100)
    urinalysis = models.CharField(max_length=100)
    urine_culture = models.CharField(max_length=100)

    rubella = models.CharField(max_length=100)
    hepatitis_b = models.CharField(max_length=100)
    hepatitis_c = models.CharField(max_length=100)
    sexual_transmitted_diseases = models.CharField(max_length=100)
    tb = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Special Early Test'
        verbose_name_plural = 'Special Early Tests'



class SpecialTestDoneLaterData(models.Model):
    glucose_screening = models.CharField(max_length=100)
    gbs = models.CharField(max_length=100)
    urinalysis = models.CharField(max_length=100)
    urine_culture = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Special Test Done Later'
        verbose_name_plural = 'Special Tests Done Later'

class ReportsData(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    data = models.CharField(max_length=250)

    class Meta:
        verbose_name = 'Report'
        verbose_name_plural = 'Reports'
    


class Notification(models.Model):
    recipient= models.EmailField()
    sender = models.EmailField()
    header = models.CharField(max_length=50)
    msg = models.CharField(max_length=250)

    class Meta:
        verbose_name = 'Notification'
        verbose_name_plural = 'Notifications'


