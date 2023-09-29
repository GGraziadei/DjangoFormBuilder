from django.db import models

class Form(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

class Field(models.Model):
    FORM_FIELD_TYPES = [
        ('text', 'Campo testuale'),
        ('number', 'Campo numerico'),
        ('multiselect', 'Multi-selezione'),
        ('email', 'Email'),
        ('date', 'Data'),
    ]

    form = models.ForeignKey(Form, on_delete=models.CASCADE)
    label = models.CharField(max_length=255)
    field_type = models.CharField(max_length=20, choices=FORM_FIELD_TYPES)
    required = models.BooleanField(default=False)
