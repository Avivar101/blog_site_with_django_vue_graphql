# Generated by Django 4.1.3 on 2022-11-21 18:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='blog.profile'),
        ),
    ]
