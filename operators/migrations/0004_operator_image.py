# Generated by Django 2.2.5 on 2019-09-22 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operators', '0003_auto_20190921_1510'),
    ]

    operations = [
        migrations.AddField(
            model_name='operator',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]