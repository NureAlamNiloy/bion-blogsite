# Generated by Django 4.2.3 on 2023-09-02 09:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0002_blogpost_title_tag'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpost',
            name='image',
        ),
    ]