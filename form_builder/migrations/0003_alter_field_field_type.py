# Generated by Django 4.2.5 on 2023-09-29 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form_builder', '0002_field_choices'),
    ]

    operations = [
        migrations.AlterField(
            model_name='field',
            name='field_type',
            field=models.CharField(choices=[('text', 'Campo testuale'), ('number', 'Campo numerico'), ('multiselect', 'Multi-selezione'), ('email', 'Email'), ('date', 'Data'), ('file', 'Carica file')], max_length=20),
        ),
    ]
