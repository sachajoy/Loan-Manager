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
        return "{} - {} - {}".format(self.name, self.taluka_id, self.taluka_id.district_id)

    def get_absolute_url(self):
        return reverse('loan:list-village')

class Faliya(models.Model):
    village_id = models.ForeignKey(Village, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    def __str__(self):
        return "{} - {} - {} - {}".format(self.name,
                                self.village_id,
                                self.village_id.taluka_id,
                                self.village_id.taluka_id.district_id )

    def get_absolute_url(self):
        return reverse('loan:list-faliya')