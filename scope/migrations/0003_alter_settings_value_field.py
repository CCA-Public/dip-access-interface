# Generated by Django 2.2.12 on 2020-04-22 17:58

import jsonfield.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [("scope", "0002_initial_data")]

    operations = [
        migrations.AlterField(
            model_name="setting",
            name="value",
            field=jsonfield.fields.JSONField(max_length=500),
        )
    ]