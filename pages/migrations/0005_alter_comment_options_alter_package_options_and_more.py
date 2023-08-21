# Generated by Django 4.2.1 on 2023-08-21 19:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pages', '0004_package_price'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'verbose_name': 'نظر', 'verbose_name_plural': 'نظرات'},
        ),
        migrations.AlterModelOptions(
            name='package',
            options={'verbose_name': ' محصولات', 'verbose_name_plural': ' محصولات'},
        ),
        migrations.AlterField(
            model_name='comment',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author', to=settings.AUTH_USER_MODEL, verbose_name='سازنده'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='data_created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='data_modified',
            field=models.DateTimeField(auto_now=True, verbose_name='تاریخ ویرایش'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='package_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='package', to='pages.package', verbose_name='نام محصول'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='text',
            field=models.TextField(verbose_name='متن'),
        ),
        migrations.AlterField(
            model_name='package',
            name='data_created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد'),
        ),
        migrations.AlterField(
            model_name='package',
            name='description',
            field=models.TextField(blank=True, verbose_name='توضیحات'),
        ),
        migrations.AlterField(
            model_name='package',
            name='image',
            field=models.ImageField(blank=True, upload_to='media/image', verbose_name='تصویر'),
        ),
        migrations.AlterField(
            model_name='package',
            name='price',
            field=models.PositiveIntegerField(blank=True, verbose_name='قیمت'),
        ),
        migrations.AlterField(
            model_name='package',
            name='title',
            field=models.CharField(max_length=300, verbose_name='عنوان محصول'),
        ),
    ]
