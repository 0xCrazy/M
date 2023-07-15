from django.contrib import admin
from . models import *

@admin.register(EmployeeDataManager)
class EmployeeDataManagerAdmin(admin.ModelAdmin):
     #fields = ('email', 'user')
     list_display = ('name', 'email', 'is_active', 'date_joined', 'last_login', 'groups')
     ordering = ('name', )
     search_fields = ('name', 'email')

    

@admin.register(StationName)
class StationNameAdmin(admin.ModelAdmin):
     fields = (('name', 'description'), ('registration_number'), 'mobile_number', 'physical_address')
     list_display = ('name', 'description', 'registration_number', 'mobile_number', 'physical_address')
     ordering = ('name', 'registration_number')
     search_fields = ('name', 'registration_number')



@admin.register(ClientData)
class ClientDataAdmin(admin.ModelAdmin):
     
     fields = (('first_name', 'middle_name', 'last_name'), ('date_of_birth', 'gender'), 'mobile_number', 'education_level', 'curent_occupation', 'residential_address')
     list_display = ('first_name', 'middle_name', 'last_name', 'date_of_birth', 'gender', 'mobile_number', 'education_level', 'curent_occupation', 'residential_address')
     ordering = ('first_name', 'gender' )
     search_fields = ('first_name','last_name')



@admin.register(ClientsSpouseData)
class ClientsSpouseDataAdmin(admin.ModelAdmin):
     fields = ('', '')
     list_display = ('', '')
     ordering = ('', )
     search_fields = ('',)



@admin.register(MaternityData)
class MaternityDataAdmin(admin.ModelAdmin):
     fields = ('', '')
     list_display = ('', '')
     ordering = ('', )
     search_fields = ('',)




@admin.register(MenstruationData)
class MenstruationDataAdmin(admin.ModelAdmin):
     fields = ('', '')
     list_display = ('', '')
     ordering = ('', )
     search_fields = ('',)



@admin.register(SpecialTestData)
class SpecialTestDataAdmin(admin.ModelAdmin):
     fields = ('', '')
     list_display = ('', '')
     ordering = ('', )
     search_fields = ('',)




@admin.register(ReportsData)
class ReportsDataAdmin(admin.ModelAdmin):
     fields = ('', '')
     list_display = ('', '')
     ordering = ('', )
     search_fields = ('',)




@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
     fields = ('', '')
     list_display = ('', '')
     ordering = ('', )
     search_fields = ('',)






