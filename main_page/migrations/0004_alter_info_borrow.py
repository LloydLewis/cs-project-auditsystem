# Generated by Django 5.0.4 on 2024-05-02 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0003_alter_info_borrow'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='borrow',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Borrowed on'),
        ),
    ]
