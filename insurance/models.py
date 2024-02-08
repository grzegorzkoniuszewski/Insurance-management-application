from django.db import models


class PolicyStatus(models.Model):
    # Represents the status of an insurance policy.
    policy_status_name = models.CharField(max_length=15, unique=True)

    def __str__(self):
        # Returns the name of the policy status as a string representation of the object.
        return self.policy_status_name


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
    validity_end_date = models.DateField()
    # Status of the policy, linked to PolicyStatus model, indicates the current state of the policy.
    status = models.ForeignKey(
        PolicyStatus,
        verbose_name="Policy Status",
        on_delete=models.SET_NULL,  # Action to take when related object is deleted.
        null=True,  # Allows null values in the database.
    )
    # Type of the policy, linked to PolicyType model, specifies the type of the policy.
    policy_type = models.ForeignKey(
        PolicyType,
        verbose_name="Policy Type",
        on_delete=models.SET_NULL,  # Action to take when related object is deleted.
        null=True,  # Allows null values in the database.
    )

    def __str__(self):
        # Returns the policy number as a string representation of the object.
        return self.policy_number
