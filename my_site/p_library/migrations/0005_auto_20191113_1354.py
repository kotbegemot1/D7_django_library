# Generated by Django 2.2.6 on 2019-11-13 13:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('p_library', '0004_book_redact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Friend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='book',
            name='redact',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='books', to='p_library.Redaction'),
        ),
        migrations.AddField(
            model_name='book',
            name='friendbook',
            field=models.ManyToManyField(blank=True, related_name='friend', to='p_library.Friend'),
        ),
    ]