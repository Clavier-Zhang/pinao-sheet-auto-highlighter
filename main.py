from src.page import Page
from pdf2image import convert_from_path
import os
import tempfile
import img2pdf

filename = 'target.pdf'
images = convert_from_path('./'+filename, dpi=500)
for i in range(0, len(images)):
	print('Start working on page '+str(i+1))
	images[i].save('./output/'+str(i)+'.jpg', 'JPEG')

	page = Page('./output/'+str(i)+'.jpg', 350)

	# page.analyze_notes()

	# page.analyze_sharp_flat_natural()

	page.draw_page()
	page.draw_lines()
	page.draw_bars()
	# page.draw_sharp_flat_natural()
	# page.draw_notes()

	page.save('./output/'+str(i)+'.jpg')



output = open("./output/output.pdf","wb")
page_names = []
for filename in os.listdir('./output'):
	if filename.endswith(".jpg"):
		page_names.append('./output/'+filename)
page_names.sort()
pdf_bytes = img2pdf.convert(page_names)
output.write(pdf_bytes)