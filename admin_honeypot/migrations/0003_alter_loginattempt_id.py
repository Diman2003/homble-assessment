# Generated by Django 4.2.3 on 2023-07-12 02:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_honeypot', '0002_auto_20160208_0854'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loginattempt',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]