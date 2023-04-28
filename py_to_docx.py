from docxtpl import DocxTemplate


doc = DocxTemplate("template.docx")

context = {"version": "Begin 0.1.0"}
doc.render(context)
doc.save("test.docx")