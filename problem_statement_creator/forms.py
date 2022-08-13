from django import forms


# Problem Statement Creator Form
class ProblemStatementCreatorForm(forms.ModelForm):
    email = forms.EmailField(required=True, min_length=5)
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    name = forms.CharField(required=True)
    organization = forms.CharField(required=True)
    country = forms.CharField(required=True)
    organization_type = forms.CharField(required=True)
    state = forms.CharField(required=True, max_length=20)
    mobile = forms.CharField(required=True, max_length=10, min_length=10)
    city = forms.CharField(required=True, max_length=20)
    designation = forms.CharField(required=True, max_length=30)
    linked_in = forms.CharField(max_length=100)
    department = forms.CharField(max_length=100, required=True)
    nomination_letter = forms.FileField(required=True)
    terms_and_conditions = forms.BooleanField(required=True)
