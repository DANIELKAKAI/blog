# Generated by Django 2.0.3 on 2018-09-10 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20180909_2114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image_1',
            field=models.ImageField(null=True, upload_to='images'),
        ),
        migrations.AlterField(
            model_name='post',
            name='image_2',
            field=models.ImageField(null=True, upload_to='images'),
        ),
        migrations.AlterField(
            model_name='post',
            name='image_3',
            field=models.ImageField(null=True, upload_to='images'),
        ),
        migrations.AlterField(
            model_name='post',
            name='image_4',
            field=models.ImageField(null=True, upload_to='images'),
        ),
        migrations.AlterField(
            model_name='post',
            name='image_5',
            field=models.ImageField(null=True, upload_to='images'),
        ),
    ]