# Generated by Django 4.1.3 on 2022-11-15 04:40

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=100)),
                ('url', models.URLField()),
                ('fecha_carga', models.DateField(auto_now=True)),
            ],
        ),
    ]