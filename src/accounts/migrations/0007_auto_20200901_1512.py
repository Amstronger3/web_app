# Generated by Django 3.0.8 on 2020-09-01 15:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20200901_1441'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='following',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Profile.followers+', to='accounts.Profile'),
        ),
        migrations.DeleteModel(
            name='Follow',
        ),
    ]
