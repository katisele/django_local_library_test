# Generated by Django 3.2.dev20200526052607 on 2020-06-07 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_language'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='date_of_death',
        ),
        migrations.AddField(
            model_name='author',
            name='date_published',
            field=models.DateField(blank=True, null=True, verbose_name='published'),
        ),
    ]
