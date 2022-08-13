# Generated by Django 3.2.9 on 2021-11-19 23:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('problem_statement_creator', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProblemStatementSubmitted',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField(max_length=250)),
                ('dataset_file', models.FileField(upload_to='problem_statements/dataset/')),
                ('youtube_link', models.URLField(max_length=100)),
                ('technology', models.CharField(choices=[('IoT', 'IoT'), ('Data Science', 'Data Science'), ('Machine Learning', 'Machine Learning'), ('Artificial Intelligence', 'Artificial Intelligence'), ('Mechatronics', 'Mechatronics'), ('Others', 'Others')], max_length=50)),
                ('domain_bucket', models.CharField(choices=[('Agriculture and Rural Development', 'Agriculture and Rural Development'), ('Clean Water', 'Clean Water'), ('Robotics & Drones', 'Robotics & Drones'), ('Healthcare & Biomedical Devices', 'Healthcare & Biomedical Devices'), ('Energy / Renewable Energy', 'Energy / Renewable Energy'), ('Security & Surveillance', 'Security & Surveillance'), ('Smart Communication', 'Smart Communication'), ('Smart Vehicles', 'Smart Vehicles'), ('Software - Mobile App development', 'Software - Mobile App development'), ('Miscellaneous', 'Miscellaneous'), ('Software - Web App development', 'Software - Web App development'), ('Travel and Tourism', 'Travel and Tourism'), ('Finance', 'Finance'), ('Life Sciences', 'Life Sciences'), ('Waste Management', 'Waste Management'), ('Food Technology', 'Food Technology'), ('Smart Education', 'Smart Education'), ('Smart Cities', 'Smart Cities'), ('Sports and Fitness', 'Sports and Fitness'), ('Smart Textiles', 'Smart Textiles'), ('Sustainable Environment', 'Sustainable Environment')], max_length=50)),
                ('category_bucket', models.CharField(max_length=100)),
                ('is_approved', models.BooleanField(default=False)),
                ('is_rejected', models.BooleanField(default=False)),
                ('submitted_by', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='problem_statement_creator.problemstatementcreator')),
            ],
        ),
    ]