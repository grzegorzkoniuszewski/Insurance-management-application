from django.db import models
from TUBase.models import CustomTUBase
from accounts.models import CustomUser


class PolicyStatus(models.Model):
    # Reprezentuje status polisy ubezpieczeniowej.
    policy_status_name = models.CharField(max_length=15, unique=True)

    def __str__(self):
        # Zwraca nazwę statusu polisy jako reprezentację obiektu w postaci ciągu znaków.
        return self.policy_status_name

    class Meta:
        verbose_name = "Status polisy"
        verbose_name_plural = "Statusy polis"


class PolicyType(models.Model):
    policy_type_name = models.CharField(max_length=25)

    def __str__(self):
        return self.policy_type_name


class InsurancePolicy(models.Model):
    tuBase = models.ForeignKey(
        CustomTUBase,
        verbose_name="Towarzystwo ubezpieczeniowe",
        on_delete=models.SET_NULL,
        null=True,
    )

    policy_number = models.CharField(max_length=11, unique=True)

    validity_start_date = models.DateField()

    validity_end_date = models.DateField()
    policy_creator = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)

    status = models.ForeignKey(
        PolicyStatus,
        verbose_name="Status polisy",
        on_delete=models.SET_NULL,
        null=True,
    )

    policy_type = models.ForeignKey(
        PolicyType,
        verbose_name="Typ polisy",
        on_delete=models.SET_NULL,
        null=True,
    )

    def __str__(self):

        return self.policy_number

    class Meta:
        verbose_name = "Insurance policy"
        verbose_name_plural = "Insurance policies"
