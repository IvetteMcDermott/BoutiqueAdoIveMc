# Generated by Django 3.2 on 2023-03-27 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20230327_1038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='has_sizes',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
    ]
