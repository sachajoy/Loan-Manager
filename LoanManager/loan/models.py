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
        return reverse('loan:detial-client', kwargs={'pk': self.id})


class Vehical(models.Model):
    company = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    model = models.CharField(max_length=255)

    class Meta:
        unique_together = ('company', 'name')

    def __str__(self):
        return self.name + ", " + self.company

    def get_absolute_url(self):
        return reverse('loan:vehical-list')


class Loan(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    vehical = models.ForeignKey(Vehical, on_delete=models.CASCADE)
    reg_no = models.CharField(max_length=50)
    agrmnt_date = models.DateField()
    chasis_no = models.CharField(max_length=50)
    engine_no = models.CharField(max_length=50)
    principle_amt = models.IntegerField()
    intrest_rate = models.FloatField()
    emi_amt = models.FloatField()
    months = models.IntegerField()

    class Meta:
        unique_together = ('reg_no', 'chasis_no', 'engine_no')

    def __str__(self):
        return "{} - {}".format(self.vehical_id, self.client_id)

    def get_absolute_url(self):
        return reverse('loan:loan-detail')


class Emi(models.Model):
    client_id = models.ForeignKey(Client, on_delete=models.CASCADE)
    loan_id = models.ForeignKey(Loan, on_delete=models.CASCADE)
    emi_amt = models.FloatField(null=True, default=0)
    amt = models.FloatField(null=True, default=0)
    due_date = models.DateField()
    paid_date = models.DateField(null=True)
    receipt_no = models.CharField(max_length=20, null=True)
    remarks = models.TextField(null=True)
    penalty = models.IntegerField()

    def __str__(self):
        return "{} - {}".format(self.due_date, self.loan_id)

    def get_absolute_url(self):
        return reverse('loan:list-emi')
