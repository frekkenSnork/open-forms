# Generated by Django 2.2.24 on 2021-08-19 14:24

import uuid

import django.contrib.postgres.fields.jsonb
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("forms", "0032_merge_20210817_1420"),
    ]

    operations = [
        migrations.AlterField(
            model_name="formlogic",
            name="actions",
            field=django.contrib.postgres.fields.jsonb.JSONField(
                help_text="Which action(s) to perform if the JSON logic evaluates to true.",
                verbose_name="actions",
            ),
        ),
        migrations.AlterField(
            model_name="formlogic",
            name="form",
            field=models.ForeignKey(
                help_text="Form to which the JSON logic applies.",
                on_delete=django.db.models.deletion.CASCADE,
                to="forms.Form",
            ),
        ),
        migrations.AlterField(
            model_name="formlogic",
            name="uuid",
            field=models.UUIDField(
                default=uuid.uuid4, unique=True, verbose_name="UUID"
            ),
        ),
    ]