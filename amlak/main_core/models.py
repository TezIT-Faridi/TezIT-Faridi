from django.db import models
from .sample import Date, Karbari


class Mahale(models.Model):
    name = models.CharField('نام محله', max_length=100)


class FuruOrMojAll(models.Model):
    directionlist = (
        ('N', 'شمالی'),
        ('S', 'جنوبی'),
        ('W', 'غربی'),
        ('E', 'شرقی'),
        ('DoKale', 'دو کله'),
        ('SeBar', 'سه بر'),
        ('NW', 'شمالی - غربی'),
        ('NE', 'شمالی - شرقی'),
        ('SW', 'جنوبی - غربی'),
        ('SE', 'جنوبی - شرقی'),
    )
    sukunatlist = (
        ('Takhlie', 'تخلیه'),
        ('Ejare', 'اجاره'),
        ('Malek', 'سکونت مالک')
    )
    mahale = models.ForeignKey(Mahale, verbose_name='نام محله', on_delete=models.PROTECT)
    address = models.CharField('آدرس', max_length=200)
    direction = models.CharField('جهت زمین', choices=directionlist, max_length=50)
    sukunat_status = models.CharField('وضعیت سکونت', choices=sukunatlist, max_length=20)
    description = models.TextField('توضیحات')
    sanad_status = models.CharField('وضعیت سند', max_length=50, null=True, blank=True)
    c_date = Date.c
    e_date = Date.e


class FuruOrMojImages(models.Model):

    file = models.ForeignKey(FuruOrMojAll, on_delete=models.CASCADE)
    image = models.ImageField()


class FuruOrMojAparEdarKolang(models.Model):

    floor_count = models.IntegerField('تعداد طبقات')
    unit_count = models.IntegerField('تعداد واحد')
    zir_bana = models.IntegerField('زیربنا')
    sen_bana = models.IntegerField('سن بنا')


class FurOrMojAparEdar(models.Model):
    kitchen_list = (
        ('MDF', 'MDF'),
        ('memberan', 'ممبران'),
        ('wood', 'چوبی'),
        ('metal', 'فلزی'),
        ('enzo', 'انزو'),
        ('yes', 'دارد بدون توضیحات'),
        ('no', 'ندارد')
    )
    floor = models.IntegerField('طبقه')
    room = models.IntegerField('طبقه')
    kitchen = models.CharField('سرویس آشپزخانه', choices=kitchen_list,max_length=20)
    elevator = models.BooleanField('آسانسور')


class FuruOrMojAparEdarTejar(models.Model):
    wc_list = (
        ('irani', 'ّایرانی'),
        ('farangi', 'فرنگی'),
        ('iranfar', 'ایرانی و فرنگی'),
        ('no', 'ندارد'),
    )
    kafpoosh_list = (
        ('stone', 'سنگ'),
        ('ceramik', 'سرامیک'),
        ('laminat', 'لمینت'),
        ('parket', 'پارکت'),
        ('mozaeik', 'موزاییک'),
        ('moket', 'موکت'),
    )

    tel = models.IntegerField('تعداد خط تلفن' )
    wc = models.CharField('سرویس بهداشتی', choices=wc_list,max_length=20)
    parking = models.IntegerField('تعداد پارکینگ')
    basement = models.IntegerField('متراژ انباری')
    balkon = models.BooleanField('بالکن')
    kafpoosh = models.CharField('کفپوش', choices=kafpoosh_list,max_length=20)
    heater = models.CharField('گرمایش', max_length=100)
    cooler = models.CharField('سرمایش', max_length=100)

class FuruOrMojAparteman(models.Model):
    sanad = Karbari.karbaristatus
    open_kitchen = models.BooleanField('آسپزخانه اوپن')
    masahat_zamin = models.IntegerField('مساحت زمین')
    tol_bar = models.IntegerField('طول بر', null=True, blank=True)

class FuruOrMojTejari(models.Model):

    tol_bar = models.IntegerField('دهانه ملک')


class FuruOrMojKolangi(models.Model):

    masahat_zamin = models.IntegerField('مساحت زمین')
    sanad = Karbari.karbaristatus
    tol_bar = models.IntegerField('طول بر')


class FuruOrMojZamin(models.Model):

    masahate_zamin = models.IntegerField('مساحت زمین', null=True, blank=True)
    tule_bar = models.IntegerField('طول بر', null=True, blank=True)
    sanad = Karbari.karbaristatus


class KharOrEjAll(models.Model):
    metraj = models.IntegerField('متراژ')
    mahale = models.ForeignKey(Mahale, verbose_name='نام محله', on_delete=models.PROTECT)
    description = models.TextField('توضیحات')


class KharOrEjAparEdar(models.Model):
    parking = models.BooleanField('پارکینگ')
    anbar = models.BooleanField('انباری')
    elevator = models.BooleanField('آسانسور')


class KharOrEjImages(models.Model):

    file = models.ForeignKey(KharOrEjAll, on_delete=models.CASCADE)
    image = models.ImageField()