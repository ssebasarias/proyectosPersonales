import pandas as pd
from docxtpl import DocxTemplate
from datetime import datetime

# Cargar la plantilla una vez
doc = DocxTemplate("./plantilla.docx")

universidad = "UNIVERSIDAD DE MANIZALES"
fecha = datetime.today().strftime("%d %b, %Y")

my_context = {'universidad': universidad, 'fecha': fecha}

df = pd.read_excel('./Carreras.xlsx')

for index, fila in df.iterrows():
    context = {'carrera': fila['Carreras de Ingenieria']}

    context.update(my_context)

    doc.render(context)
    doc.save(f"carrera - {fila['Carreras de Ingenieria']}.docx")