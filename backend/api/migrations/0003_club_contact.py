# Generated by Django 3.2.5 on 2021-07-29 00:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20210116_1339'),
    ]

    operations = [
        migrations.AddField(
            model_name='club',
            name='contact',
            field=models.EmailField(blank=True, max_length=254),
        ),
    ]
