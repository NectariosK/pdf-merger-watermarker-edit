#pdf-merger-watermarker-edit
#Check out-->https://pythonhosted.org/PyPDF2/PdfFileReader.html

'''
import  PyPDF2

with open('dummy.pdf', 'rb') as file: #rb stands for read the binary
	#print(file)
	reader = PyPDF2.PdfFileReader(file)
	#print(reader.numPages)
	#print(reader.getPage(1))
	reader.getPage(0)
	page = reader.getPage(0)
	page.rotateCounterClockwise(90)
	writer = PyPDF2.PdfFileWriter()
	writer.addPage(page)
	with open('tilt.pdf', 'wb') as new_file:
		writer.write(new_file)
'''

#COMBINE PDFs OR MERGE PDFs
#Command--->python pdf.py [FIRST PDF NAME].pdf [SECOND PDF NAME].pdf ..and so on and so forth
import PyPDF2
import sys

inputs = sys.argv[1:]

def pdf_combiner(pdf_list):
	merger = PyPDF2.PdfFileMerger() #merger object with PyPDF2
	for pdf in pdf_list:
		print(pdf)
		merger.append(pdf)
	merger.write('PREFERRED PDF NAME.pdf')

pdf_combiner(inputs)

'''
#WATERMARKER
import PyPDF2

template = PyPDF2.PdfFileReader(open('super.pdf', 'rb'))
watermark = PyPDF2.PdfFileReader(open('wtr.pdf', 'rb'))
output = PyPDF2.PdfFileWriter()

for i in range(template.getNumPages()):
	page = template.getPage(i)
	page.mergePage(watermark.getPage(0))
	output.addPage(page)

	with open('watermarked_output.pdf', 'wb') as file:
		output.write(file)
'''