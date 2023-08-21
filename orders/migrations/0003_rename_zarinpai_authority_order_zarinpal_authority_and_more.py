# Generated by Django 4.2.1 on 2023-08-21 19:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pages', '0005_alter_comment_options_alter_package_options_and_more'),
        ('orders', '0002_order_zarinpai_authority_order_zarinpal_data_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='zarinpai_authority',
            new_name='zarinpal_authority',
        ),
        migrations.AlterField(
            model_name='order',
            name='address',
            field=models.CharField(max_length=700, verbose_name='ادرس'),
        ),
        migrations.AlterField(
            model_name='order',
            name='data_created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد'),
        ),
        migrations.AlterField(
            model_name='order',
            name='data_modified',
            field=models.DateTimeField(auto_now=True, verbose_name='تاریخ ویرایش'),
        ),
        migrations.AlterField(
            model_name='order',
            name='first_name',
            field=models.CharField(max_length=100, verbose_name='نام'),
        ),
        migrations.AlterField(
            model_name='order',
            name='is_paid',
            field=models.BooleanField(default=False, verbose_name='پرداخت شده '),
        ),
        migrations.AlterField(
            model_name='order',
            name='last_name',
            field=models.CharField(max_length=100, verbose_name='نام خانوادگی'),
        ),
        migrations.AlterField(
            model_name='order',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, verbose_name='شماره تلفن'),
        ),
        migrations.AlterField(
            model_name='order',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='کاربر'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='orders.order', verbose_name='آیدی سفارش'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='price',
            field=models.PositiveIntegerField(verbose_name='قیمت'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_items', to='pages.package', verbose_name='آیدی محصول'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='quantity',
            field=models.PositiveIntegerField(default=1, verbose_name='تعداد'),
        ),
    ]
