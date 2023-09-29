import datetime
import json
from django.shortcuts import render
from .models import Form, Field, FormSubmission
from .forms import DynamicForm
from django.core.serializers.json import DjangoJSONEncoder

def custom_json_conversion(obj):
    if isinstance(obj, datetime.date):
        return obj.strftime('%Y-%m-%d')  # Format the date as a string
    raise TypeError

def create_form(request, form_id):
    form = Form.objects.get(pk=form_id)
    form_fields = Field.objects.filter(form=form)
    
    if request.method == 'POST':
        dynamic_form = DynamicForm(request.POST, form_fields=form_fields)
        if dynamic_form.is_valid():
            # Puoi gestire qui i dati del form inviati dal cliente e salvarli nel database
            # ad esempio, puoi creare un nuovo oggetto Model basato sui dati del form e salvarlo
            submission_data = {}
        for field in form_fields:
            field_name = field.label.lower().replace(" ", "_")
            submission_data[field_name] = dynamic_form.cleaned_data[field_name]
        json_data = json.dumps(submission_data, cls=DjangoJSONEncoder, default=custom_json_conversion)
        FormSubmission.objects.create(form=form, submission_data=json_data)
    else:
        dynamic_form = DynamicForm(form_fields=form_fields)

    return render(request, 'create_form.html', {'form': form, 'dynamic_form': dynamic_form})

