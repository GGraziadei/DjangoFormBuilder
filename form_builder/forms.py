from django import forms
from .models import Field

class DynamicForm(forms.Form):
    def __init__(self, *args, **kwargs):
        form_fields = kwargs.pop('form_fields', None)

        super(DynamicForm, self).__init__(*args, **kwargs)

        if form_fields:
            for field in form_fields:
                field_name = field.label.lower().replace(" ", "_")
                if field.field_type == 'text':
                    self.fields[field_name] = forms.CharField(
                        label=field.label,
                        required=field.required
                    )
                elif field.field_type == 'number':
                    self.fields[field_name] = forms.FloatField(
                        label=field.label,
                        required=field.required
                    )
                elif field.field_type == 'multiselect':
                    choices = [(option, option) for option in field.get_choices()]
                    self.fields[field_name] = forms.MultipleChoiceField(
                        label=field.label,
                        choices=choices,
                        widget=forms.CheckboxSelectMultiple,
                        required=field.required
                    )
                elif field.field_type == 'email':
                    self.fields[field_name] = forms.EmailField(
                        label=field.label,
                        required=field.required
                    )
                elif field.field_type == 'date':
                    self.fields[field_name] = forms.DateField(
                        label=field.label,
                        required=field.required,
                        widget=forms.DateInput(attrs={'type': 'date'})
                    )
                elif field.field_type == 'file':  # Aggiungi la gestione del campo "file"
                    self.fields[field_name] = forms.FileField(
                        label=field.label,
                        required=field.required
                    )
