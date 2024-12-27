import pandas as pd

# Cargar el archivo Excel
ruta_excel = "datos_peticionarios.xlsx"

try:
    # Leer el archivo Excel en un DataFrame
    datos = pd.read_excel(ruta_excel)
    
    # Validar que el archivo Excel tiene las columnas requeridas
    columnas_requeridas = [
        "Nombre completo del peticionario",
        "Número de documento del peticionario",
        "Dirección del peticionario",
        "Teléfono del peticionario",
        "Correo electrónico del peticionario"
    ]

    for columna in columnas_requeridas:
        if columna not in datos.columns:
            raise ValueError(f"El archivo Excel no contiene la columna requerida: {columna}")

    print("Validación del archivo Excel completada. Todas las columnas requeridas están presentes.")

    # Mostrar las primeras filas para verificar la lectura
    print("Datos cargados correctamente:")
    print(datos.head())
except FileNotFoundError:
    print(f"El archivo '{ruta_excel}' no se encontró. Asegúrate de que esté en la misma carpeta que este script.")
except Exception as e:
    print(f"Ocurrió un error al leer el archivo: {e}")


from docx import Document

# Ruta de la plantilla de Word
ruta_plantilla = "plantilla_demanda.docx"

def generar_documento(persona, ruta_plantilla, salida):
    """
    Genera un documento personalizado basado en la plantilla de Word.
    
    :param persona: Diccionario con la información de una persona.
    :param ruta_plantilla: Ruta al archivo de la plantilla de Word.
    :param salida: Nombre del archivo de salida.
    """
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

# Iterar sobre los datos del Excel
for index, fila in datos.iterrows():
    # Convertir cada fila a un diccionario
    persona = fila.to_dict()

    # Obtener el nombre del peticionario (asegúrate de que coincida con el encabezado en el Excel)
    nombre_peticionario = persona["Nombre completo del peticionario"]

    # Reemplazar espacios y caracteres especiales para nombres válidos de archivos
    nombre_archivo = f"demanda_{nombre_peticionario.replace(' ', '_').replace('/', '_')}.docx"

    # Generar el documento
    generar_documento(persona, ruta_plantilla, nombre_archivo)

import os

# Ruta de la carpeta donde se guardarán los documentos
carpeta_salida = "documentos_generados"

print("Iniciando el proceso de generación de documentos...\n")

# Crear la carpeta si no existe
if not os.path.exists(carpeta_salida):
    os.makedirs(carpeta_salida)
    print(f"Carpeta creada: {carpeta_salida}")

# Contador de documentos generados
contador = 0

# Iterar sobre los datos del Excel y generar los documentos
for index, fila in datos.iterrows():
    persona = fila.to_dict()
    nombre_peticionario = persona["Nombre completo del peticionario"]
    nombre_archivo = f"demanda_{nombre_peticionario.replace(' ', '_').replace('/', '_')}.docx"
    ruta_completa = os.path.join(carpeta_salida, nombre_archivo)

    try:
        generar_documento(persona, ruta_plantilla, ruta_completa)
        contador += 1
    except Exception as e:
        print(f"Error al generar el documento para {nombre_peticionario}: {e}")

print(f"\nProceso completado. Se generaron {contador} documentos.")
