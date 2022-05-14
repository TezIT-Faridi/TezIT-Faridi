from main_core.models import  KharOrEjAll, KharOrEjAparEdar
from django.db import models


class Aparteman(models.Model):

    kharorejall = models.OneToOneField(KharOrEjAll, on_delete=models.CASCADE)
    kharorejaparedar = models.OneToOneField(KharOrEjAparEdar, on_delete=models.CASCADE)
    khab = models.IntegerField('تعداد خواب')
    vahed = models.IntegerField('تعداد واحد')
