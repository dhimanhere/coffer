# Generated by Django 5.0 on 2024-02-06 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='myModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('end_year', models.DateField(blank=True, null=True)),
                ('intensity', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('sector', models.CharField(blank=True, max_length=255, null=True)),
                ('topic', models.CharField(blank=True, max_length=55, null=True)),
                ('insight', models.TextField()),
                ('url', models.URLField(max_length=300)),
                ('region', models.CharField(blank=True, max_length=50, null=True)),
                ('start_year', models.DateField(blank=True, null=True)),
                ('impact', models.CharField(blank=True, max_length=255, null=True)),
                ('added', models.DateTimeField(blank=True, null=True)),
                ('published', models.DateTimeField(blank=True, null=True)),
                ('country', models.CharField(blank=True, max_length=50, null=True)),
                ('relevance', models.PositiveIntegerField(blank=True, null=True)),
                ('pestle', models.CharField(blank=True, max_length=100, null=True)),
                ('source', models.CharField(blank=True, max_length=200, null=True)),
                ('title', models.CharField(blank=True, max_length=300, null=True)),
                ('likelihood', models.PositiveIntegerField(blank=True, null=True)),
            ],
        ),
    ]