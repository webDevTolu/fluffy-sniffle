# Generated by Django 4.0.5 on 2022-06-27 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_project_heroimageurl_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='heroImageUrl',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='project',
            name='previewImageUrl',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
