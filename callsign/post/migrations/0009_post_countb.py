# Generated by Django 4.1.3 on 2022-11-15 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0008_dislike_post_dislike_user_set'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='countB',
            field=models.IntegerField(max_length=30, null='True'),
            preserve_default='True',
        ),
    ]
