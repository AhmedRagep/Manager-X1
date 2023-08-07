from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
# Create your models here.

# serial=(
#     ("1000", "1000"),
#     ("1001", "1001"),
#     ("1002", "1002"),
#     ("1003", "1003"),
#     ("1004", "1004"),
#     ("1005", "1005"),
#     ("1006", "1006"),
#     ("1007", "1007"),
#     ("1008", "1008"),
# )

MONTH = (
    ('يناير 1', 'January'),
    ('فبراير 2','February'),
    ('مارس 3' ,'March') ,

)

class Person(models.Model):
    code      = models.IntegerField(null=True)
    name      = models.CharField(max_length=100)
    month     = models.CharField(max_length=50,default='')
    year      = models.CharField(max_length=50,default='')
    created_at =models.DateTimeField(default=timezone.now)
    basic     = models.CharField(max_length=30,default='')
    ntur_allow  = models.CharField(max_length=30,default='')
    trnsport_allow= models.CharField(max_length=30,default='')
    meal_allow = models.CharField(max_length=30,default='')
    phone_allow = models.CharField(max_length=30,default='')
    total = models.CharField(max_length=30,default='')
    rwrd = models.CharField(max_length=30,default='')
    rwrd_details = models.CharField(max_length=100,default='')
    over_time = models.CharField(max_length=30,default='')
    hours = models.CharField(max_length=30,default='')
    special_allow = models.CharField(max_length=30,default='')
    special_details  = models.CharField(max_length=30,default='')
    total_attidtions = models.CharField(max_length=30,default='')
    penalties = models.CharField(max_length=30,default='')
    pnlts_details= models.CharField(max_length=30,default='')
    absences = models.CharField(max_length=30,default='')
    absences_day= models.CharField(max_length=30,default='')
    insurances= models.CharField(max_length=30,default='')
    income_tax= models.CharField(max_length=30,default='')
    medical_service= models.CharField(max_length=30,default='')
    loans= models.CharField(max_length=30,default='')
    deductions_hours= models.CharField(max_length=30,default='')
    detail_hours = models.CharField(max_length=30,default='')
    car_deductions = models.CharField(max_length=30,default='')
    another_deductions = models.CharField(max_length=30,default='')
    total_deductions = models.CharField(max_length=30,default='')
    net_salary = models.CharField(max_length=30,default='')

    def __str__(self):
        return str(self.name) + " " + str(self.code)

# class Serial(models.Model):
#     serialnumer = models.()

