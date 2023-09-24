# Generated by Django 4.2.1 on 2023-09-11 16:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_text', models.TextField(verbose_name='user_text')),
                ('admin_text', models.TextField(blank=True, verbose_name='admin_text')),
                ('datetime_user_created', models.TimeField(auto_now_add=True, verbose_name='datetime_user_created')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contact_us', to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
        ),
    ]