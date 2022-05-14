from django.db import models
from main_core.sample import Date

class Customer(models.Model):

    def __str__(self):
        return 'Name: {}, Phone: {}'.format(self.last_name, self.phone)

    first_name = models.CharField('نام', max_length=20, null=True, blank=True)
    last_name = models.CharField('نام خانوادگی', max_length=30)
    phone = models.IntegerField('تلفن', null=False, blank=False)
    sex = models.BooleanField('جنسیت', blank=True, null=True)
    pic = models.ImageField(null=True, blank=True)
    c_date = Date.c
    e_date = Date.e