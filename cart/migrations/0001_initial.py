# Generated by Django 5.1.1 on 2024-10-10 16:13

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('gpu', '0002_alter_gpu_image'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Дата и время создания заказа.', verbose_name='Дата создания')),
                ('user', models.ForeignKey(help_text='Пользователь, оформивший заказ.', on_delete=django.db.models.deletion.CASCADE, related_name='cart', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1, help_text='Количество заказанных пластинок.', verbose_name='Количество')),
                ('order', models.ForeignKey(help_text='Заказ, к которому относится этот элемент.', on_delete=django.db.models.deletion.CASCADE, related_name='items', to='cart.order', verbose_name='Заказ')),
                ('gpu', models.ForeignKey(help_text='Видеокарта, которую пользователь заказал.', on_delete=django.db.models.deletion.CASCADE, to='gpu.gpu', verbose_name='Видеокарта')),
            ],
            options={
                'verbose_name': 'Элемент заказа',
                'verbose_name_plural': 'Элементы заказа',
            },
        ),
    ]
