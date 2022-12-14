# Generated by Django 4.0.4 on 2022-06-07 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0013_article_snippet'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
        migrations.AlterField(
            model_name='article',
            name='snippet',
            field=models.CharField(max_length=100),
        ),
    ]
