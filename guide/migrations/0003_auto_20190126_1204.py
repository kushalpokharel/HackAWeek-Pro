# Generated by Django 2.0.4 on 2019-01-26 06:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('guide', '0002_userprofileinfo_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofileinfo',
            name='user',
        ),
        migrations.DeleteModel(
            name='UserProfileInfo',
        ),
    ]
