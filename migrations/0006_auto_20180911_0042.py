# Generated by Django 2.0.3 on 2018-09-10 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20180910_1751'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('tech-and-gadgets', 'tech & gadgets'), ('fashion-and-style', 'fashion & style'), ('home-and-living', 'home & living')], max_length=20),
        ),
    ]
