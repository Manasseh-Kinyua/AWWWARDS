# Generated by Django 4.0.3 on 2022-04-10 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('awards', '0003_project_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='location',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
