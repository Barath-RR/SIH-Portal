# Generated by Django 3.2.9 on 2021-11-20 01:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('problem_statement_creator', '0002_nodalofficernomination_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nodalofficernomination',
            name='submitted_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='problem_statement_creator.problemstatementcreator'),
        ),
    ]
