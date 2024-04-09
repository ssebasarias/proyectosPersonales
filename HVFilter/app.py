from flask import Flask, render_template, request
import PyPDF2

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/buscar', methods=['POST'])
def buscar_palabra():
    palabra_buscada = request.form['palabra']
    archivos_pdf = request.files.getlist('pdfs')
    
    resultados = []
    
    for pdf in archivos_pdf:
        with open(pdf, 'rb') as pdf_file_obj:
            pdf_reader = PyPDF2.PdfFileReader(pdf_file_obj)
            num_pages = pdf_reader.numPages
            for page in range(num_pages):
                page_obj = pdf_reader.getPage(page)
                text = page_obj.extractText()
                if palabra_buscada.lower() in text.lower():
                    resultados.append(f"La palabra '{palabra_buscada}' se encuentra en el archivo: {pdf.filename}")
                    break
            else:
                resultados.append(f"La palabra '{palabra_buscada}' no se encuentra en el archivo: {pdf.filename}")
    
    mensaje = f"Se realizó la búsqueda en los archivos PDF seleccionados."
    
    return render_template('resultados.html', mensaje=mensaje, resultados=resultados)

if __name__ == '__main__':
    app.run(debug=True)
