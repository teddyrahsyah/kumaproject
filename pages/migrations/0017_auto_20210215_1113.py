# Generated by Django 2.2 on 2021-02-15 04:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0016_servicepagecontent_images'),
    ]

    operations = [
        migrations.RenameField(
            model_name='servicepagecontent',
            old_name='images',
            new_name='img',
        ),
    ]
