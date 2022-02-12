# Generated by Django 3.2.9 on 2022-01-31 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('topic', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('venue', models.CharField(max_length=256)),
                ('title', models.CharField(max_length=256)),
                ('info', models.TextField()),
                ('link', models.URLField(max_length=256)),
                ('docs', models.URLField(max_length=256)),
                ('headline_event', models.BooleanField(default=False)),
                ('image', models.ImageField(blank=True, upload_to='event-images/')),
                ('topics', models.ManyToManyField(blank=True, to='topic.Topic')),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
    ]