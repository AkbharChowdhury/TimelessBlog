# Generated by Django 4.0.4 on 2022-06-07 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0010_alter_article_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='snippets',
            field=models.CharField(default='click blog to...', max_length=100),
        ),
    ]
