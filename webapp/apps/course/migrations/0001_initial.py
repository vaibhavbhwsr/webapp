# Generated by Django 4.2.5 on 2023-09-20 19:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Course",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("modified_at", models.DateTimeField(auto_now=True, db_index=True)),
                (
                    "is_deleted",
                    models.BooleanField(
                        default=False, help_text="Used for soft delete"
                    ),
                ),
                ("title", models.CharField(max_length=255)),
                ("description", models.TextField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "instructor",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            managers=[
                ("all_object", django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name="Section",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True, db_index=True)),
                ("modified_at", models.DateTimeField(auto_now=True, db_index=True)),
                (
                    "is_deleted",
                    models.BooleanField(
                        default=False, help_text="Used for soft delete"
                    ),
                ),
                ("title", models.CharField(max_length=255)),
                (
                    "course",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="course.course"
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            managers=[
                ("all_object", django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name="Video",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True, db_index=True)),
                ("modified_at", models.DateTimeField(auto_now=True, db_index=True)),
                (
                    "is_deleted",
                    models.BooleanField(
                        default=False, help_text="Used for soft delete"
                    ),
                ),
                ("title", models.CharField(max_length=255)),
                ("video_file", models.FileField(upload_to="videos/course/")),
                ("duration", models.DurationField()),
                (
                    "section",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="course.section"
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            managers=[
                ("all_object", django.db.models.manager.Manager()),
            ],
        ),
    ]
