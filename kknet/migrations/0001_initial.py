# Generated by Django 5.0.7 on 2024-08-02 03:26

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Icecream',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.IntegerField(verbose_name='')),
                ('mfr', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=100)),
                ('img', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Discountinfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('pw_hash', models.CharField(max_length=128)),
                ('ice_cream', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kknet.icecream')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)])),
                ('content', models.TextField()),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('pw_hash', models.CharField(max_length=128)),
                ('ice_cream', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kknet.icecream')),
            ],
        ),
    ]