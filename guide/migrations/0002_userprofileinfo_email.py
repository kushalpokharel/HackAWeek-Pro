# Generated by Django 2.0.4 on 2019-01-26 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guide', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofileinfo',
            name='email',
            field=models.EmailField(default='', max_length=254),
            preserve_default=False,
        ),
    ]
