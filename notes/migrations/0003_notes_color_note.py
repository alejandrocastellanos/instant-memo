# Generated by Django 3.2.15 on 2023-02-09 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0002_alter_notes_dead_line'),
    ]

    operations = [
        migrations.AddField(
            model_name='notes',
            name='color_note',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
