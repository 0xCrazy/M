from django.contrib import admin
from . models import *

admin.site.register(User)

    

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
     #fields = ('client', 'first')
     list_display = ('client', 'first_name', 'middle_name', 'last_name', 'date_of_birth', 'age', 'gender', 'mobile_number', 'education_level', 'curent_occupation', 'residential_address')
     ordering = ('client', 'last_name' )
     search_fields = ('client', 'last_name')



@admin.register(MaternityData)
class MaternityDataAdmin(admin.ModelAdmin):
     #fields = ('', '')
     list_display = ('client', 'birth_number', 'number_of_time_given_birth', 'living_children', 'miscariages', 'year_of_miscariage')
     ordering = ('client', 'year_of_miscariage' )
     search_fields = ('client', 'year_of_miscariage')




@admin.register(MenstruationData)
class MenstruationDataAdmin(admin.ModelAdmin):
     fields = ('client', 'period_length', 'cycle_length', 'start_date', 'end_date')
     list_display = ('client', 'period_length', 'cycle_length')
     ordering = ('client', )
     search_fields = ('client','cycle_length')



@admin.register(SpecialTestData)
class SpecialTestDataAdmin(admin.ModelAdmin):
     fields = ('complete_blood_count', 'blood_type', 'urinalysis', 'urine_culture', 'rubella', 'hepatitis_b', 'hepatitis_c', 'sexual_transmitted_diseases', 'tb')
     list_display = ('complete_blood_count', 'blood_type', 'urinalysis', 'urine_culture', 'rubella', 'hepatitis_b', 'hepatitis_c', 'sexual_transmitted_diseases', 'tb')
     ordering = ('complete_blood_count','blood_type')
     search_fields = ('complete_blood_count', 'blood_type')



@admin.register(SpecialTestDoneLaterData)
class SpecialTestDoneLaterDataAdmin(admin.ModelAdmin):
     fields = ('glucose_screening', 'gbs', 'urinalysis', 'urine_culture')
     list_display = ('glucose_screening', 'gbs', 'urinalysis', 'urine_culture')
     ordering = ('glucose_screening','gbs')
     search_fields = ('glucose_screening','gbs')



@admin.register(ReportsData)
class ReportsDataAdmin(admin.ModelAdmin):
     fields = ('client', 'data')
     list_display = ('client', 'data')
     ordering = ('client', )
     search_fields = ('client', 'data')




@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
     
     list_display = ('recipient', 'sender', 'header', 'msg')
     ordering = ('recipient', 'header')
     search_fields = ('recipient', 'header')






