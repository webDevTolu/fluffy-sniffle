# Generated by Django 4.0.5 on 2022-06-25 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255)),
                ('description', models.CharField(blank=True, max_length=255)),
                ('codeUrl', models.URLField()),
                ('liveDemoUrl', models.URLField()),
                ('previewImageUrl', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('heroImageUrl', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('body', models.CharField(blank=True, max_length=255)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
