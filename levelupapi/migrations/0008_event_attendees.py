# Generated by Django 3.2 on 2021-05-11 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('levelupapi', '0007_remove_event_joined'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='attendees',
            field=models.ManyToManyField(related_name='attending', through='levelupapi.GameEvent', to='levelupapi.Gamer'),
        ),
    ]
