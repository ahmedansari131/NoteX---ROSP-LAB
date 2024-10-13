# Generated by Django 4.2.6 on 2024-10-13 08:46

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="NoteLabel",
            fields=[
                ("name", models.CharField(max_length=50, unique=True)),
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Note",
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
                ("title", models.CharField(max_length=500)),
                ("description", models.CharField(max_length=10000)),
                ("created_at", models.DateTimeField(auto_now=True)),
                ("updated_at", models.DateTimeField(auto_now_add=True)),
                ("pinned", models.BooleanField(default=False)),
                ("archived", models.BooleanField(default=False)),
                ("color", models.CharField(blank=True, default="", max_length=50)),
                (
                    "note_image",
                    models.CharField(
                        blank=True, default="", max_length=1000, null=True
                    ),
                ),
                (
                    "note_image_public_id",
                    models.CharField(
                        blank=True, default="", max_length=1000, null=True
                    ),
                ),
                ("labels", models.ManyToManyField(blank=True, to="crud.notelabel")),
            ],
        ),
    ]
