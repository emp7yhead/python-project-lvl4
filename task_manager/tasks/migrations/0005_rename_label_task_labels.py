# Generated by Django 4.0.4 on 2022-06-30 16:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0004_tasklabels_alter_task_label_tasklabels_task'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='label',
            new_name='labels',
        ),
    ]
