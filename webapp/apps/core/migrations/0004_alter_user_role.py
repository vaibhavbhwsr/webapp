# Generated by Django 4.2.5 on 2023-09-20 16:56

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0003_alter_user_role"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="role",
            field=models.CharField(
                blank=True,
                choices=[
                    ("Instructor", "Instructor"),
                    ("Learner", "Learner"),
                    ("Other", "Other"),
                    ("None", None),
                ],
                default="Learner",
                max_length=200,
                null=True,
            ),
        ),
    ]
