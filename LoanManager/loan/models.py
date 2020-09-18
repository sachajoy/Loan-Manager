from django.db import models
from django.shortcuts import reverse


class District(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('loan:list-district')


class Taluka(models.Model):
    district_id = models.ForeignKey(District, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    def __str__(self):
        return "{} - {}".format(self.name, self.district_id)

    def get_absolute_url(self):
        return reverse('loan:list-taluka')


class Village(models.Model):
    taluka_id = models.ForeignKey(Taluka, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    def __str__(self):
        return "{} - {}".format(self.name, self.taluka_id)

    def get_absolute_url(self):
        return reverse('loan:list-village')


class Faliya(models.Model):
    village_id = models.ForeignKey(Village, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    def __str__(self):
        return "{} - {}".format(self.name, self.village_id)

    def get_absolute_url(self):
        return reverse('loan:list-faliya')


class Firm(models.Model):
    name = models.CharField(max_length=255)
    abv = models.CharField(max_length=10)

    def __str__(self):
        return self.abv

    def get_absolute_url(self):
        return reverse('loan:create-client')


class Client(models.Model):
    firm_id = models.ForeignKey(Firm, on_delete=models.CASCADE)
    challan_no = models.IntegerField()
    file_no = models.CharField(max_length=15)
    fname = models.CharField(max_length=50)
    mname = models.CharField(max_length=50, null=True)
    lname = models.CharField(max_length=50)
    addr = models.CharField(max_length=255)
    faliya = models.ForeignKey(Faliya, on_delete=models.CASCADE)
    mob_no = models.CharField(max_length=11)
    gtr = models.CharField(max_length=100)
    gtr_mob_no = models.CharField(max_length=11)

    class Meta:
        unique_together = ('firm_id', 'challan_no', 'file_no')
    def __str__(self):
        return "{} {}, {}".format(self.fname, self.lname, self.mob_no)

    def get_absolute_url(self):
        return reverse('loan:list-client')
