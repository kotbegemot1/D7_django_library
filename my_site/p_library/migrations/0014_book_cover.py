# Generated by Django 2.2.6 on 2019-11-26 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('p_library', '0013_book_publisher'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='cover',
            field=models.ImageField(blank=True, upload_to='covers/%Y/%m/%d'),
        ),
    ]
