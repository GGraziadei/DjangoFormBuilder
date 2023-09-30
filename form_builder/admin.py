from django.contrib import admin
from django.http import HttpResponse

from form_builder.utils import generate_excel_report
from .models import Form, Field, FormSubmission

class FieldInline(admin.TabularInline):  # Puoi anche utilizzare StackedInline se preferisci una visualizzazione impilata
    model = Field

@admin.register(Form)
class FormAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    # Aggiungi eventuali altre opzioni di visualizzazione e filtraggio dei dati del modello Form
    inlines=[FieldInline]

class FormSubmissionAdmin(admin.ModelAdmin):
    list_display = ('form', 'submission_date')
    actions = ['download_report']

    def download_report(self, request, queryset):
        # Qui inserisci la logica per generare il report Excel
        # E ottenere il file_path del report
        file_path = generate_excel_report(queryset)
        # Restituisci il file Excel come download
        with open(file_path, 'rb') as excel_file:
            response = HttpResponse(excel_file.read(), content_type='application/ms-excel')
            response['Content-Disposition'] = f'attachment; filename=report.xlsx'
        return response

    download_report.short_description = 'Download Report'

admin.site.register(FormSubmission, FormSubmissionAdmin)