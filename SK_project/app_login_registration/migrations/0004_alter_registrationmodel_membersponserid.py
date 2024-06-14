# Generated by Django 5.0.6 on 2024-05-09 19:57

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_login_registration', '0003_rename_id_registrationmodel_membersponserid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registrationmodel',
            name='memberSponserId',
            field=models.UUIDField(default=uuid.uuid1, editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]
