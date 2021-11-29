# Generated by Django 2.2.24 on 2021-11-29 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0003_fix_duplicate_emails"),
    ]

    operations = [
        migrations.AddConstraint(
            model_name="user",
            constraint=models.UniqueConstraint(
                condition=models.Q(_negated=True, email=""),
                fields=("email",),
                name="filled_email_unique",
            ),
        ),
    ]
