# Generated by Django 3.2.5 on 2021-07-09 18:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('endereco', '0001_initial'),
        ('core', '0005_pontoturistico_avaliacoes'),
    ]

    operations = [
        migrations.AddField(
            model_name='pontoturistico',
            name='endereco',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='endereco.endereco'),
            preserve_default=False,
        ),
    ]
