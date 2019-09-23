# Generated by Django 2.2.5 on 2019-09-22 18:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('operators', '0004_operator_image'),
        ('turn', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=120)),
                ('surname', models.CharField(max_length=120)),
                ('code', models.CharField(blank=True, max_length=40, null=True)),
                ('state', models.IntegerField(choices=[(1, 'Waiting'), (2, 'Working'), (3, 'Endup')], default=1)),
                ('operators_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='turn', to='operators.Operator')),
                ('service', models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, related_name='turn', to='operators.Service')),
            ],
            options={
                'ordering': ['created'],
            },
        ),
        migrations.DeleteModel(
            name='Turn',
        ),
    ]
