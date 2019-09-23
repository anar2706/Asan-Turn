# Generated by Django 2.2.5 on 2019-09-22 19:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('operators', '0004_operator_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='operator',
            name='service',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='operators', to='operators.Service'),
        ),
    ]
