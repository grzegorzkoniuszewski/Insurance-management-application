from django.db import models
from datetime import timedelta


class PolicyStatus(models.Model):
    # Represents the status of an insurance policy.
    policy_status_name = models.CharField(max_length=15, unique=True)

    def __str__(self):
        # Returns the name of the policy status as a string representation of the object.
        return self.policy_status_name

    class Meta:
        verbose_name = "Policy status"
        verbose_name_plural = "Policy status"


class PolicyType(models.Model):
    # Represents the type of an insurance policy.
    # Name of the policy type.
    policy_type_name = models.CharField(max_length=25)

    def __str__(self):
        # Returns the name of the policy type as a string representation of the object.
        return self.policy_type_name


class InsurancePolicy(models.Model):
    # Represents an insurance policy.
    # Policy number, unique for each policy.
    policy_number = models.CharField(max_length=11, unique=True)
    # Start date of policy validity.
    validity_start_date = models.DateField()
    # End date of policy validity.
    validity_end_date = models.DateField(editable=False)  # Making the field non-editable in admin
    # Status of the policy, linked to PolicyStatus model, indicates the current state of the policy.
    status = models.ForeignKey(
        PolicyStatus,
        verbose_name="Policies Status",
        on_delete=models.SET_NULL,  # Action to take when related object is deleted.
        null=True,  # Allows null values in the database.
    )
    # Type of the policy, linked to PolicyType model, specifies the type of the policy.
    policy_type = models.ForeignKey(
        PolicyType,
        verbose_name="Policies Type",
        on_delete=models.SET_NULL,  # Action to take when related object is deleted.
        null=True,  # Allows null values in the database.
    )

    def save(self, *args, **kwargs):
        # Calculate the end date of policy validity to be one year minus one day from the start date
        leap_year = self.validity_start_date.year % 4 == 0 and (
                    self.validity_start_date.year % 100 != 0 or self.validity_start_date.year % 400 == 0)
        days_in_year = 366 if leap_year else 365
        self.validity_end_date = self.validity_start_date + timedelta(days=days_in_year - 1)
        super().save(*args, **kwargs)

    def __str__(self):
        # Returns the policy number as a string representation of the object.
        return self.policy_number
