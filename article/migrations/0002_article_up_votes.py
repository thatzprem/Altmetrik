# Generated by Django 2.1.2 on 2018-10-02 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='up_votes',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
