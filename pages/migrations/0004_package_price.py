# Generated by Django 4.2.1 on 2023-07-20 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_alter_comment_package_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='package',
            name='price',
            field=models.PositiveIntegerField(blank=True, default=500, verbose_name='price'),
            preserve_default=False,
        ),
    ]