# Generated by Django 4.2.3 on 2023-07-19 10:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='selling_prince',
            new_name='selling_price',
        ),
    ]