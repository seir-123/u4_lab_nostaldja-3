# Generated by Django 4.1.7 on 2023-03-29 20:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nostaldja', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fad',
            name='description',
        ),
        migrations.RemoveField(
            model_name='fad',
            name='image_url',
        ),
        migrations.RemoveField(
            model_name='fad',
            name='name',
        ),
        migrations.AlterField(
            model_name='fad',
            name='decade',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fads', to='nostaldja.decade'),
        ),
    ]