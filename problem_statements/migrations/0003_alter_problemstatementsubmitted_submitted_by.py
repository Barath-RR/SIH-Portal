# Generated by Django 3.2.9 on 2021-11-20 01:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('problem_statement_creator', '0003_alter_nodalofficernomination_submitted_by'),
        ('problem_statements', '0002_auto_20211120_0617'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problemstatementsubmitted',
            name='submitted_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='problem_statement_creator.problemstatementcreator'),
        ),
    ]
