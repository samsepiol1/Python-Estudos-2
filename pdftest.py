import PyPDF2
content=''
f=open('curriculum_vitae_modelo.pdf','rb')
pdf=PyPDF2.PdfFileReader(f)
print(pdf.getNumPages())
for i in range(0,pdf.getNumPages()):
    content += pdf.getPage(i).extractText() + "\n"
var_control=content.split()
print(content)
qualidades=['Microsoft','Linux','Corel Draw']
for var_control in qualidades:
    print('Chamar Para entrevista {}'.format(qualidades[0]))
    print('Chamar para ')



