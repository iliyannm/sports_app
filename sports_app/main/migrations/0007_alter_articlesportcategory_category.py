# Generated by Django 4.0.3 on 2022-03-30 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_remove_article_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlesportcategory',
            name='category',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]
