# Generated by Django 3.1.5 on 2021-01-21 13:21

from django.db import migrations

def forwards_func(apps,schema_editor):
    db_alias = schema_editor.connection.alias

    Group = apps.get_model("auth", "Group")
    # Permission = apps.get_model("auth", "Permission")

    Group.objects.using(db_alias).bulk_create(
        [Group(name="customer"),
         Group(name="specialist")]
    )
    # group_customer = Group.objects.using(db_alias).filter(name='customer').first()
    # group_customer.permissions.add(Permission.objects.using(db_alias).get_or_create(codename='can_become_specialist'))

def reverse_func(apps, schema_editor):
    db_alias = schema_editor.connection.alias

    Group = apps.get_model("auth", "Group")
    Group.objects.using(db_alias).filter(name = 'customer').delete()
    Group.objects.using(db_alias).filter(name = 'specialist').delete()


class Migration(migrations.Migration):

    dependencies = [
        ('specialistservice', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(forwards_func, reverse_func)
    ]