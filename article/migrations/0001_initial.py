# Generated by Django 2.1.2 on 2018-10-02 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identifier', models.CharField(blank=True, max_length=50, null=True)),
                ('title', models.CharField(blank=True, max_length=250, null=True)),
                ('content', models.CharField(blank=True, max_length=100, null=True)),
                ('author_name', models.CharField(blank=True, max_length=100, null=True)),
                ('created', models.DateTimeField(blank=True, editable=False, null=True)),
                ('modified', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]