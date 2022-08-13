from django.db import models


# Problem Statement Creators Profile
class ProblemStatementCreator(models.Model):
    ps_creator_id = models.AutoField(primary_key=True)
    email = models.EmailField(blank=False)
    name = models.CharField(blank=False, max_length=50)
    organization = models.CharField(blank=False, max_length=50)
    country = models.CharField(default="India", blank=False, max_length=30)
    organization_type = models.CharField(blank=False, max_length=30)
    state = models.CharField(blank=False, max_length=30)
    mobile = models.CharField(blank=False, max_length=10)
    city = models.CharField(blank=False, max_length=30)
    designation = models.CharField(blank=False, max_length=50)
    linked_in = models.CharField(blank=True, max_length=100)
    department = models.CharField(blank=False, max_length=50)
    nomination_letter = models.FileField(upload_to="problem_statement_creator/nominations", blank=False)
    is_email_verified = models.BooleanField(blank=False, default=False)
    is_mobile_verified = models.BooleanField(blank=False, default=False)
    first_login = models.DateTimeField(auto_now=True)
    is_approved = models.BooleanField(blank=False, default=False)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Problem Statement Creator"
        verbose_name_plural = "Problem Statement Creators"


# Nodal Officer Nomination
class NodalOfficerNomination(models.Model):
    non_id = models.AutoField(primary_key=True)
    email = models.EmailField(blank=False)
    name = models.CharField(blank=False, max_length=50)
    organization = models.CharField(blank=False, max_length=50)
    country = models.CharField(default="India", blank=False, max_length=30)
    organization_type = models.CharField(blank=False, max_length=30)
    state = models.CharField(blank=False, max_length=30)
    mobile = models.CharField(blank=False, max_length=10)
    city = models.CharField(blank=False, max_length=30)
    designation = models.CharField(blank=False, max_length=50)
    linked_in = models.CharField(blank=True, max_length=100)
    department = models.CharField(blank=False, max_length=50)
    submitted_by = models.ForeignKey(ProblemStatementCreator, blank=False, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    is_approved = models.BooleanField(default=False)
    is_rejected = models.BooleanField(default=False)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Nominated Nodal Officers"
        verbose_name_plural = "Nominated Nodal Officers"
