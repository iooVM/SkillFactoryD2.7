# Generated by Django 3.2.6 on 2021-08-27 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_alter_category_categorya'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='categorya',
            field=models.CharField(max_length=32, unique=True),
        ),
    ]
