from django_jalali.db import models as jmodels
from django.db import models

class Date():
    c = jmodels.jDateField('تاریخ ایجاد', auto_now_add=True)
    e = jmodels.jDateField('تاریخ آخرین تغییر', auto_now=True)

class Karbari():
    karbaristatuslist = (
        ('Maskuni', 'مسکونی'),
        ('Tejari', 'تجاری'),
        ('Edari', 'اداری'),
        ('MoEdari', 'موقعیت اداری'),
        ('Baq', 'باغ'),
        ('Vila', 'ویلایی'),
    )
    karbaristatus = models.CharField('کاربری', choices=karbaristatuslist,max_length=20)

class Furushande():
    price = models.IntegerField('قیمت')

class Mojer():
    rahn = models.IntegerField('رهن')
    ejare = models.IntegerField('اجاره')
    tabdil = models.BooleanField('قابل تبدیل')


