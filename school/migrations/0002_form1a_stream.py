# Generated by Django 4.1.6 on 2023-02-06 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='form1a',
            name='stream',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]