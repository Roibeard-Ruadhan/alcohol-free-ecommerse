# Generated by Django 3.2 on 2022-06-04 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20220604_1031'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogcomment',
            name='published',
            field=models.BooleanField(default=False),
        ),
    ]
