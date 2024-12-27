from django import forms

class DocumentUploadForm(forms.Form):
    archivo_excel = forms.FileField(
        label="Subir archivo Excel",
        help_text="Sube un archivo Excel con los datos necesarios para generar los documentos."
    )
