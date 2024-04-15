import glob
import PyPDF2

# Palabra a buscar
palabra_buscada = "python"

# Obtener la lista de archivos PDF en la carpeta
pdf_files = glob.glob('carpeta/*.pdf')

# Iterar sobre cada archivo PDF
for pdf_file in pdf_files:
    # Abrir el archivo PDF en modo de lectura binaria
    pdf_file_obj = open(pdf_file, 'rb')

    # Crear un objeto de lectura de PDF
    pdf_reader = PyPDF2.PdfFileReader(pdf_file_obj)

    # Obtener el número de páginas del PDF
    num_pages = pdf_reader.getNumPages()

    # Bandera para indicar si se encontró la palabra en el PDF
    palabra_encontrada = False

    # Iterar sobre cada página del PDF
    for page in range(num_pages):
        # Obtener el objeto de la página
        page_obj = pdf_reader.getPage(page)

        # Extraer el texto de la página
        text = page_obj.extract_text()

        # Verificar si la palabra buscada está presente en el texto
        if palabra_buscada.lower() in text.lower():
            # Imprimir el nombre del archivo PDF si se encontró la palabra
            print(f"La palabra '{palabra_buscada}' se encuentra en el archivo: {pdf_file}")

            # Marcar la bandera como True
            palabra_encontrada = True
            break

    # Cerrar el archivo PDF
    pdf_file_obj.close()

    # Imprimir un mensaje si la palabra no se encontró en el PDF
    if not palabra_encontrada:
        print(f"La palabra '{palabra_buscada}' no se encuentra en el archivo: {pdf_file}")