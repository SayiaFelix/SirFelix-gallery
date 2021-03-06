# Generated by Django 3.2 on 2022-05-28 12:13

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('category_name', models.CharField(max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('location_name', models.CharField(max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('image_name', models.CharField(max_length=30)),
                ('image_descriptions', models.TextField()),
                ('post_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('image', models.ImageField(null=True, upload_to='images/')),
                ('category', models.ManyToManyField(to='myBooth.category')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myBooth.location')),
            ],
        ),
    ]
