from django.db import models


# Create your models here.
class loandetails(models.Model):
    userid = models.CharField(max_length=30)
    loan_no = models.IntegerField()
    loan_amount = models.IntegerField()
    loan_tenure = models.IntegerField()
    loan_roi = models.FloatField()
    loan_date = models.DateField()
    surety_no = models.IntegerField()
    surety_name = models.CharField(max_length=30)

    def __str__(self):
        return str(self.loan_no)


class memberdetails(models.Model):
    userid = models.CharField(max_length=30)
    memberno = models.IntegerField()
    memebername = models.CharField(max_length=30)
    mobileno = models.CharField(max_length=30)

    def __str__(self):
        return str(self.memberno)


class profiledetails(models.Model):
    userid = models.CharField(max_length=30)
    membername = models.CharField(max_length=30)
    memberno = models.IntegerField()
    memberclass = models.CharField(max_length=20)
    employeecode = models.CharField(max_length=20)
    soceityname = models.CharField(max_length=20)

    def __str__(self):
        return str(self.memberno)


class transactions(models.Model):
    userid = models.CharField(max_length=30)
    date = models.DateField()
    amount = models.IntegerField()
    transactionmode = models.CharField(max_length=30)
    heading = models.CharField(max_length=30)
    receiotorcharges = models.CharField(max_length=20)
    description = models.CharField(max_length=50)

    def __str__(self):
        return str(self.userid)


class outstanding(models.Model):
    userid = models.CharField(max_length=30)
    lop = models.CharField(max_length=30)
    los = models.CharField(max_length=30)
    td = models.CharField(max_length=30)
    share = models.CharField(max_length=20)

    def __str__(self):
        return str(self.userid)
