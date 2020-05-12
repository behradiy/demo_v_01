# Generated by Django 3.0.5 on 2020-05-11 18:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('Image', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Commoditie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('Price', models.BigIntegerField()),
                ('SelesNumber', models.IntegerField()),
                ('Popularity', models.IntegerField()),
                ('Views', models.IntegerField()),
                ('AmountinStore', models.IntegerField()),
                ('About', models.CharField(max_length=5000)),
                ('image', models.ImageField(upload_to='')),
                ('Category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='commodity.Category')),
                ('Marketer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]