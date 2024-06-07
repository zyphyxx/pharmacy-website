# Generated by Django 5.0.6 on 2024-06-07 18:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Types',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='types',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='products.types'),
        ),
    ]
