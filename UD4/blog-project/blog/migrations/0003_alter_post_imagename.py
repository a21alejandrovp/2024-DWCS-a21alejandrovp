# Generated by Django 4.2.17 on 2025-02-10 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_post_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='imageName',
            field=models.ImageField(null=True, upload_to='images'),
        ),
    ]
