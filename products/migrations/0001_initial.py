# Generated by Django 5.0.1 on 2024-01-12 20:14

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255, unique=True)),
                ('eliminado', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20, unique=True)),
                ('eliminado', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Talla',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20, unique=True)),
                ('eliminado', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_id', models.CharField(db_column='codigo_id', max_length=100, unique=True)),
                ('nombre', models.CharField(db_column='nombre', max_length=255)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('imagen', models.ImageField(null=True, upload_to='productos')),
                ('material', models.CharField(max_length=20)),
                ('temporada', models.CharField(max_length=20)),
                ('ocasión', models.CharField(max_length=20)),
                ('descripción', models.TextField()),
                ('stock', models.IntegerField()),
                ('disponibilidad', models.BooleanField()),
                ('fecha_creación', models.DateTimeField(auto_now_add=True)),
                ('fecha_actualización', models.DateTimeField(auto_now=True)),
                ('eliminado', models.BooleanField(default=False)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='products.categoria')),
                ('colores', models.ManyToManyField(to='products.color')),
                ('creador', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='productos_creados', to=settings.AUTH_USER_MODEL)),
                ('modificador', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='productos_modificados', to=settings.AUTH_USER_MODEL)),
                ('tallas', models.ManyToManyField(to='products.talla')),
            ],
        ),
    ]
