# Generated by Django 3.1.7 on 2021-03-07 17:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20210307_1741'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='shopID',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.shop'),
        ),
    ]
