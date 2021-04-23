# Generated by Django 3.2 on 2021-04-20 20:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0006_estados'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('telefone', models.IntegerField()),
                ('rua', models.CharField(max_length=200)),
                ('numero', models.IntegerField()),
                ('bairro', models.CharField(max_length=200)),
                ('cidade', models.CharField(max_length=200)),
                ('bio', models.TextField()),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]