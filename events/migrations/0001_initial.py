# Generated by Django 3.2.9 on 2022-02-27 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('start_datetime', models.DateTimeField()),
                ('finish_datetime', models.DateTimeField()),
                ('address', models.TextField()),
                ('content', models.TextField()),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('thumbnail', models.ImageField(upload_to='events/')),
                ('institute', models.CharField(choices=[('SC', 'Shrinathji College'), ('SS', 'Shrinathji School')], max_length=5)),
            ],
        ),
    ]