from django.db import models
from main_core.models import FuruOrMojZamin, FuruOrMojAll, FuruOrMojAparEdarKolang, FurOrMojAparEdar, FuruOrMojAparEdarTejar
from main_core.models import FuruOrMojAparteman, FuruOrMojTejari, FuruOrMojKolangi
from main_core.sample import Mojer


class Maskuni(models.Model):

    furuall = models.OneToOneField(FuruOrMojAll, on_delete=models.CASCADE)
    aprkolangedar = models.OneToOneField(FuruOrMojAparEdarKolang, on_delete=models.CASCADE)
    aparedar = models.OneToOneField(FurOrMojAparEdar, on_delete=models.CASCADE)
    aparedartejar = models.OneToOneField(FuruOrMojAparEdarTejar, on_delete=models.CASCADE)
    aprteman = models.OneToOneField(FuruOrMojAparteman, on_delete=models.CASCADE)
    rahn = Mojer.rahn
    ejare = Mojer.ejare
    tabdil = Mojer.tabdil

class Edari(models.Model):

    furuall = models.OneToOneField(FuruOrMojAll, on_delete=models.CASCADE)
    aprkolangedar = models.OneToOneField(FuruOrMojAparEdarKolang, on_delete=models.CASCADE)
    aparedar = models.OneToOneField(FurOrMojAparEdar, on_delete=models.CASCADE)
    aparedartejar = models.OneToOneField(FuruOrMojAparEdarTejar, on_delete=models.CASCADE)
    rahn = Mojer.rahn
    ejare = Mojer.ejare
    tabdil = Mojer.tabdil


class Tejari(models.Model):

    furuall = models.OneToOneField(FuruOrMojAll, on_delete=models.CASCADE)
    aparedartejar = models.OneToOneField(FuruOrMojAparEdarTejar, on_delete=models.CASCADE)
    tejari = models.OneToOneField(FuruOrMojTejari, on_delete=models.CASCADE)
    rahn = Mojer.rahn
    ejare = Mojer.ejare
    tabdil = Mojer.tabdil


class Kolangi(models.Model):

    furuall = models.OneToOneField(FuruOrMojAll, on_delete=models.CASCADE)
    aprkolangedar = models.OneToOneField(FuruOrMojAparEdarKolang, on_delete=models.CASCADE)
    kolangi = models.OneToOneField(FuruOrMojKolangi, on_delete=models.CASCADE)
    rahn = Mojer.rahn
    ejare = Mojer.ejare
    tabdil = Mojer.tabdil



class Zamin(models.Model):

    furuall = models.OneToOneField(FuruOrMojAll, on_delete=models.CASCADE)
    furu_zamin = models.OneToOneField(FuruOrMojZamin, on_delete=models.CASCADE)
    rahn = Mojer.rahn
    ejare = Mojer.ejare
    tabdil = Mojer.tabdil