# Generated by Django 4.1.2 on 2022-11-03 13:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Tables', '0005_ipc_sections'),
    ]

    operations = [
        migrations.CreateModel(
            name='Judgements',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('judgements_description', models.CharField(max_length=100)),
                ('judgement_SC', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Tables.ipc_sections')),
            ],
        ),
    ]
