# Generated by Django 3.2.16 on 2023-03-04 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallpage', '0004_follow'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Follow',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='followers',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='following',
            field=models.IntegerField(default=0),
        ),
    ]