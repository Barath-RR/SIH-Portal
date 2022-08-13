from django.db import models
from problem_statement_creator.models import ProblemStatementCreator

choices = (
    ("Hardware", "Hardware"),
    ("Software", "Software")
)
domain = (
    ("Agriculture and Rural Development", "Agriculture and Rural Development"),
    ("Clean Water", "Clean Water"),
    ("Robotics & Drones", "Robotics & Drones"),
    ("Healthcare & Biomedical Devices", "Healthcare & Biomedical Devices"),
    ("Energy / Renewable Energy", "Energy / Renewable Energy"),
    ("Security & Surveillance", "Security & Surveillance"),
    ("Smart Communication", "Smart Communication"),
    ("Smart Vehicles", "Smart Vehicles"),
    ("Software - Mobile App development", "Software - Mobile App development"),
    ("Miscellaneous", "Miscellaneous"),
    ("Software - Web App development", "Software - Web App development"),
    ("Travel and Tourism", "Travel and Tourism"),
    ("Finance", "Finance"),
    ("Life Sciences", "Life Sciences"),
    ("Waste Management", "Waste Management"),
    ("Food Technology", "Food Technology"),
    ("Smart Education", "Smart Education"),
    ("Smart Cities", "Smart Cities"),
    ("Sports and Fitness", "Sports and Fitness"),
    ("Smart Textiles", "Smart Textiles"),
    ("Sustainable Environment", "Sustainable Environment"),

)

tech = (
    ("IoT", "IoT"),
    ("Data Science", "Data Science"),
    ("Machine Learning", "Machine Learning"),
    ("Artificial Intelligence", "Artificial Intelligence"),
    ("Mechatronics", "Mechatronics"),
    ("Others", "Others"),
)


# Problem Statements
class ProblemStatementSubmitted(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=250, blank=False, unique=True)
    description = models.TextField(max_length=1000, blank=False)
    dataset_file = models.FileField(upload_to='problem_statements/dataset/', blank=True)
    youtube_link = models.URLField(max_length=100, blank=True)
    technology = models.CharField(choices=tech, max_length=50, blank=False)
    domain_bucket = models.CharField(choices=domain, max_length=50, blank=False)
    category = models.CharField(max_length=100, blank=False)
    submitted_by = models.ForeignKey(ProblemStatementCreator, blank=False, on_delete=models.CASCADE)
    is_approved = models.BooleanField(default=False)
    is_rejected = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Problem Statements Submitted by Problem Statement Creators"
        verbose_name_plural = "Problem Statements Submitted by Problem Statement Creators"
