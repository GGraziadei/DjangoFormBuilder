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
        ('file', 'Carica file'),  # Aggiungi il nuovo tipo di campo "file"
    ]

    form = models.ForeignKey(Form, on_delete=models.CASCADE)
    label = models.CharField(max_length=255)
    field_type = models.CharField(max_length=20, choices=FORM_FIELD_TYPES)
    required = models.BooleanField(default=False)
    choices = models.TextField(blank=True, null=True, help_text='Inserisci le scelte, separate da una virgola (es. Opzione 1, Opzione 2)')

    def get_choices(self):
        if self.field_type == 'multiselect':
            return [choice.strip() for choice in self.choices.split(',') if choice.strip()]
        return []

    def __str__(self):
        return self.label

class FormSubmission(models.Model):
    form = models.ForeignKey(Form, on_delete=models.CASCADE)
    submission_data = models.JSONField()  # Salva i dati del form in formato JSON
    submission_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Submission for {self.form.name} - {self.submission_date}"