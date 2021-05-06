# Generated by Django 3.2 on 2021-05-06 15:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('levelupapi', '0002_gameType'),
    ]

    operations = [
        migrations.RenameField(
            model_name='game',
            old_name='name',
            new_name='title',
        ),
        migrations.RemoveField(
            model_name='game',
            name='description',
        ),
        migrations.AddField(
            model_name='game',
            name='gamer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='levelupapi.gamer'),
        ),
        migrations.AddField(
            model_name='game',
            name='maker',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='game',
            name='number_of_players',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='game',
            name='skill_level',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
    ]