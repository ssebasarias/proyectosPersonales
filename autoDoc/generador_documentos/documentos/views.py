from django.shortcuts import render
from django.http import FileResponse, HttpResponse
from .forms import DocumentUploadForm
import pandas as pd
import os
from docx import Document
from django.conf import settings
import zipfile

# --- Generar documentos con plantillas específicas ---
# Función para generar el documento
def generar_documento(persona, ruta_plantilla, salida):
    try:
        # Cargar la plantilla
        doc = Document(ruta_plantilla)

        # Reemplazar las variables en la plantilla
        for parrafo in doc.paragraphs:
            for llave, valor in persona.items():
                if f"{{{{{llave}}}}}" in parrafo.text:  # Busca {{variable}}
                    parrafo.text = parrafo.text.replace(f"{{{{{llave}}}}}", str(valor))

        # Guardar el documento modificado
        doc.save(salida)
        print(f"Documento generado: {salida}")
    except Exception as e:
        print(f"Ocurrió un error al generar el documento: {e}")

# Mapeo de plantillas según el tipo y subtipo de proceso
# Mapeo de plantillas según el tipo y subtipo de proceso
PLANTILLAS = {
    "Demanda": {
        "Civil": os.path.join(settings.MEDIA_ROOT, "templates", "demanda_civil.docx"),
        "Penal": os.path.join(settings.MEDIA_ROOT, "templates", "demanda_penal.docx"),
        "Laboral": os.path.join(settings.MEDIA_ROOT, "templates", "demanda_laboral.docx"),
    },
    "Derecho de Petición": os.path.join(settings.MEDIA_ROOT, "templates", "derecho_peticion.docx"),
    "Otro": os.path.join(settings.MEDIA_ROOT, "templates", "proceso_generico.docx"),
}


# --- Procesar Excel y generar documentos ---
# Vista para cargar y procesar los archivos
def upload_files(request):
    if request.method == 'POST':
        form = DocumentUploadForm(request.POST, request.FILES)
        if form.is_valid():
            archivo_excel = request.FILES['archivo_excel']

            # Guardar el archivo Excel
            archivo_excel_path = os.path.join(settings.MEDIA_ROOT, archivo_excel.name)
            with open(archivo_excel_path, 'wb+') as destino:
                for chunk in archivo_excel.chunks():
                    destino.write(chunk)

            try:
                # Leer datos del archivo Excel
                datos = pd.read_excel(archivo_excel_path)
                carpeta_salida = os.path.join(settings.MEDIA_ROOT, "documentos_generados")
                os.makedirs(carpeta_salida, exist_ok=True)

                contador = 0
                for _, fila in datos.iterrows():
                    tipo_proceso = fila.get("Tipo de Proceso", "Otro")
                    subtipo_proceso = fila.get("Subtipo de Proceso", None)

                    # Determinar la plantilla adecuada
                    if tipo_proceso in PLANTILLAS:
                        if isinstance(PLANTILLAS[tipo_proceso], dict):
                            plantilla = PLANTILLAS[tipo_proceso].get(subtipo_proceso, PLANTILLAS["Otro"])
                        else:
                            plantilla = PLANTILLAS[tipo_proceso]
                    else:
                        plantilla = PLANTILLAS["Otro"]

                    # Datos de la persona
                    persona = fila.to_dict()
                    nombre_archivo = f"{tipo_proceso}_{subtipo_proceso}_{persona.get('Nombre completo', 'anonimo').replace(' ', '_')}.docx"
                    carpeta_tipo = os.path.join(carpeta_salida, tipo_proceso)
                    os.makedirs(carpeta_tipo, exist_ok=True)
                    ruta_salida = os.path.join(carpeta_tipo, nombre_archivo)

                    # Generar documento
                    try:
                        generar_documento(persona, plantilla, ruta_salida)
                        contador += 1
                    except Exception as e:
                        print(f"Error al generar documento: {e}")

                return render(request, 'upload_success.html', {'contador': contador})
            except Exception as e:
                print(f"Error al procesar el archivo Excel: {e}")
                return render(request, 'upload_error.html', {'error': str(e)})
    else:
        form = DocumentUploadForm()

    return render(request, 'upload_files.html', {'form': form})

# --- Descargar plantilla Excel ---
def descargar_plantilla(request):
    ruta_archivo = os.path.join("media", "plantilla_datos.xlsx")
    if os.path.exists(ruta_archivo):
        return FileResponse(open(ruta_archivo, 'rb'), as_attachment=True, filename="plantilla_datos.xlsx")
    return HttpResponse("La plantilla no está disponible.", status=404)

# --- Descargar documentos generados ---
def descargar_documentos(request, carpeta):
    carpeta_path = os.path.join(settings.MEDIA_ROOT, "documentos_generados", carpeta)
    if os.path.exists(carpeta_path):
        # Crear un archivo ZIP de la carpeta de documentos
        archivo_zip = f"{carpeta}.zip"
        ruta_zip = os.path.join(settings.MEDIA_ROOT, archivo_zip)
        
        with zipfile.ZipFile(ruta_zip, 'w') as zipf:
            for root, dirs, files in os.walk(carpeta_path):
                for file in files:
                    file_path = os.path.join(root, file)
                    zipf.write(file_path, os.path.relpath(file_path, carpeta_path))
        
        # Devolver el archivo ZIP al usuario
        return FileResponse(open(ruta_zip, 'rb'), as_attachment=True, filename=archivo_zip)
    else:
        return HttpResponse("La carpeta no existe.", status=404)

# --- Página principal ---
def home(request):
    return HttpResponse("<h1>Bienvenido al Generador de Documentos</h1>")
