# Generated by Django 4.2.1 on 2023-10-07 09:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pages', '0008_alter_package_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='is_confirmed',
            field=models.BooleanField(default=False),
        ),
        migrations.CreateModel(
            name='ReplyComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='text')),
                ('data_created', models.DateTimeField(auto_now_add=True, verbose_name='date created')),
                ('data_modified', models.DateTimeField(auto_now=True, verbose_name='date modified')),
                ('is_confirmed', models.BooleanField(default=False)),
                ('comment_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commentreply', to='pages.comment', verbose_name='reply comment name')),
                ('reply_author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reply_author', to=settings.AUTH_USER_MODEL, verbose_name='reply author')),
                ('reply_package_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reply_package_name', to='pages.package', verbose_name='reply package name')),
            ],
            options={
                'verbose_name': 'ReplyComment',
                'verbose_name_plural': 'ReplyComments',
            },
        ),
    ]
