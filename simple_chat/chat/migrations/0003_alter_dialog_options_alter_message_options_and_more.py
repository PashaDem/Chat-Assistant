# Generated by Django 4.1 on 2022-09-05 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_dialog_message'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dialog',
            options={'ordering': ['user_id'], 'verbose_name': 'Dialog', 'verbose_name_plural': 'Dialogs'},
        ),
        migrations.AlterModelOptions(
            name='message',
            options={'ordering': ['date'], 'verbose_name': 'Message', 'verbose_name_plural': 'Messages'},
        ),
        migrations.AlterField(
            model_name='dialog',
            name='user_id',
            field=models.IntegerField(verbose_name='user identifier'),
        ),
        migrations.AlterField(
            model_name='message',
            name='is_mine',
            field=models.BooleanField(default=True, verbose_name="user's message"),
        ),
        migrations.AlterField(
            model_name='message',
            name='text',
            field=models.TextField(),
        ),
    ]
