# Generated by Django 4.0.3 on 2023-03-23 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('presentations', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='status',
            name='id',
            field=models.PositiveSmallIntegerField(primary_key=True, serialize=False),
        ),
    ]
