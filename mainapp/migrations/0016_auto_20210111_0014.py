# Generated by Django 3.1.4 on 2021-01-10 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0015_auto_20210110_0205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='buying_type',
            field=models.CharField(choices=[('self', 'Самовывоз'), ('delivery', 'Доставка')], default='self', max_length=100, verbose_name='Тип заказа'),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('completed', 'Заказ выполнен'), ('new', 'Новый заказ'), ('in_progress', 'Заказ в обработке'), ('ready', 'Заказ готов')], default='new', max_length=100, verbose_name='Статус'),
        ),
        migrations.AlterField(
            model_name='specification',
            name='required',
            field=models.BooleanField(default=True, verbose_name='Обязательно для заполнение'),
        ),
    ]