# Generated by Django 4.0.4 on 2022-06-22 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_accounts_managers_accounts_is_staff_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='accounts',
            name='is_superuser',
            field=models.BooleanField(default=False),
        ),
    ]
