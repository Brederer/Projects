# Generated by Django 4.2.3 on 2023-08-02 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AD',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена')),
                ('auction', models.BooleanField(help_text='Отметьте, если торг уместен', verbose_name='Торг')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('upated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
