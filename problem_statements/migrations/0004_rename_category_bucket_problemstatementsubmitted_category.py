# Generated by Django 3.2.9 on 2021-11-20 05:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('problem_statements', '0003_alter_problemstatementsubmitted_submitted_by'),
    ]

    operations = [
        migrations.RenameField(
            model_name='problemstatementsubmitted',
            old_name='category_bucket',
            new_name='category',
        ),
    ]