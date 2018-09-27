# Generated by Django 2.1.1 on 2018-09-27 16:12

from __future__ import unicode_literals

from django.db import migrations
from django.contrib.auth.management import create_permissions

from dips.models import DublinCore, Setting


def migrate_permissions(apps, schema_editor):
    """
    Create permissions in migration before they are created in a
    post_migrate signal handler. They are needed to create the user
    group and the signal handler won't create duplicated permissions.
    This must be executed after the auth and dips apps are migrated.
    """
    for app_config in apps.get_app_configs():
        app_config.models_module = True
        create_permissions(app_config, apps=apps, verbosity=0)
        app_config.models_module = None


def add_user_groups(apps, schema_editor):
    """Create user groups with permissions."""
    Group = apps.get_model('auth', 'Group')
    Permission = apps.get_model('auth', 'Permission')
    editor_group, created = Group.objects.get_or_create(name='Editors')
    if created:
        permissions = Permission.objects.filter(codename__in=(
            'add_collection', 'change_collection',
            'add_dip', 'change_dip',
        ))
        for permision in permissions:
            editor_group.permissions.add(permision)
        editor_group.save()
    managers_group, created = Group.objects.get_or_create(name='Managers')
    if created:
        permissions = Permission.objects.filter(codename__in=(
            'add_user', 'change_user', 'delete_user',
        ))
        for permission in permissions:
            managers_group.permissions.add(permission)
        managers_group.save()
    # Viewers group is only for display purposes
    # and has no special permissions.
    Group.objects.create(name='Viewers')


def add_initial_settings(apps, schema_editor):
    """Create initial settings to manage DC fields."""
    Setting.objects.create(
        name='enabled_optional_dc_fields',
        value=list(DublinCore.get_optional_fields().keys()),
    )
    Setting.objects.create(
        name='hide_empty_dc_fields',
        value=True,
    )


def remove_user_groups(apps, schema_editor):
    Group = apps.get_model('auth', 'Group')
    Group.objects.all().delete()


def remove_initial_settings(apps, schema_editor):
    Setting.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('dips', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(migrate_permissions, migrations.RunPython.noop),
        migrations.RunPython(add_user_groups, remove_user_groups),
        migrations.RunPython(add_initial_settings, remove_initial_settings),
    ]
