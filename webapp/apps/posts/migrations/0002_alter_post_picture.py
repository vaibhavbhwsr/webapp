# Generated by Django 4.2.5 on 2023-09-20 18:39

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("posts", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="picture",
            field=models.ImageField(blank=True, upload_to="posts/"),
        ),
    ]
