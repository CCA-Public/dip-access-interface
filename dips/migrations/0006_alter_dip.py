# Generated by Django 2.1.7 on 2019-04-30 03:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [("dips", "0005_alter_dublincore_language")]

    operations = [
        migrations.RemoveField(model_name="dip", name="import_task_id"),
        migrations.AddField(
            model_name="dip",
            name="import_error",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="dip",
            name="ss_dir_name",
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name="dip",
            name="ss_download_url",
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name="dip",
            name="ss_host_url",
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name="dip",
            name="ss_uuid",
            field=models.CharField(blank=True, max_length=36, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name="dip",
            name="collection",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="dips",
                to="dips.Collection",
                verbose_name="collection",
            ),
        ),
    ]