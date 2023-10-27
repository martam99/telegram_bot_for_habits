# Generated by Django 4.2.6 on 2023-10-26 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habit', '0002_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='habit',
            options={'verbose_name': 'привычка', 'verbose_name_plural': 'привычки'},
        ),
        migrations.AlterField(
            model_name='habit',
            name='period',
            field=models.CharField(choices=[('DAILY', 'каждый день'), ('WEEKLY', 'раз в неделю')], default='DAILY', max_length=15, verbose_name='Периодичность'),
        ),
    ]
