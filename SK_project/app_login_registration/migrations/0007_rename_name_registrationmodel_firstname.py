# Generated by Django 5.0.6 on 2024-05-13 18:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_login_registration', '0006_alter_registrationmodel_membersponserid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='registrationmodel',
            old_name='name',
            new_name='firstName',
        ),
    ]
