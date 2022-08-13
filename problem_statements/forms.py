from django import forms


# Problem Statement Submission Form
class ProblemStatementSubmission(forms.Form):
    title = forms.CharField(max_length=100, required=True, min_length=10)
    description = forms.CharField(max_length=500, required=True, min_length=10)
    dataset = forms.FileField()
    youtube_link = forms.URLField()
    technology_bucket = forms.CharField(required=True, max_length=100)
    category_bucket = forms.ChoiceField(choices=(
        ('Hardware', 'Hardware'),
        ('Software', 'Software')
    ), required=True)

