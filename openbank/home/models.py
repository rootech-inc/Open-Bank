from django.conf import settings
from django.db import models


# Create your models here.
class Account(models.Model):
    acct_name = models.TextField()
    acct_pref = models.IntegerField()
    city = models.TextField()
    address = models.TextField()
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )


class AccountMore(models.Model):
    acct = models.ForeignKey('Account', on_delete=models.CASCADE)
    acct_descr = models.TextField()
    acct_no = models.CharField(max_length=12, unique=True)


class Transactions(models.Model):
    acct = models.ForeignKey('Account', on_delete=models.CASCADE)
    sub_acct = models.IntegerField(default=0)
    descr = models.TextField()

    debit = models.DecimalField(decimal_places=2,max_digits=65)
    credit = models.DecimalField(decimal_places=2,max_digits=65)
    balance = models.DecimalField(decimal_places=2,max_digits=65)

    created_on = models.DateField(auto_created=True)
    time_created = models.TimeField(auto_created=True)