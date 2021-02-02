from PyPDF2 import PdfFileWriter, PdfFileReader
from pdfminer import high_level
import os
import re

if not os.path.exists('output'):
    os.makedirs('output')

# pdf_filename = input('Enter pdf to split:')

# pdf_filename = './pdfs/_EVF_Qtrly_Form.pdf'
pdf_filename = './pdfs/_EVF_Qtrly_Form-2.pdf'
# pdf_filename = './pdfs/chris-evans-ewu.pdf'



inputpdf = PdfFileReader(open(pdf_filename, "rb"))

for i in range(inputpdf.numPages):
    # Get Name
    pages = [i] # just the first page

    extracted_text = high_level.extract_text(pdf_filename, "", pages)
    # print('===== EXTRACTED CONTENT ===== [START]')
    # print(extracted_text)
    # print('===== EXTRACTED CONTENT ===== [END]')


    print (extracted_text)
    start_keyword = 'Updated: March 2018'
    start_keyword_length = len(start_keyword)

    # print(start_keyword_length)
    start_keyword_position = extracted_text.find(start_keyword)
    # print(start_keyword_position)
    start_parse = start_keyword_position + start_keyword_length + 3 # +3 for the new line characters

    end_parse = extracted_text.find('♀')

    
    # Option 1 - Parsing Name based on fixed length Student Number (which will only work if ALL student numbers have a fixed length)
    print('Option 1')
    studentno_length = 10
    extracted_name = extracted_text[start_parse:end_parse-studentno_length]
    extracted_studentno = extracted_text[end_parse-studentno_length:end_parse]
    print('extracted_name:',extracted_name)
    print('extracted_studentno:',extracted_studentno)


    # Option 2 - Parsing both Name and Number
    print('Option 2')
    extracted_name = extracted_text[start_parse:end_parse] #contains name and number
    print('extracted_name',extracted_name)


    # Option 3 - Parsing Name by detecting the first instance of a number in the extracted text to serve as a stop position
    print('Option 3')
    s1 = extracted_text[start_parse:end_parse]
    m = re.search(r"\d", s1)
    extracted_name = ''
    if m:
        # print("Digit found at position", m.start())
        extracted_name = extracted_text[start_parse:start_parse+m.start()]
        print('extracted_name',extracted_name)
    else:
        print("No digit in that string")

    

    output = PdfFileWriter()
    output.addPage(inputpdf.getPage(i))
    outputpath = './output/'

    with open(outputpath + "SPRING_EVF_%s.pdf" % extracted_name, "wb") as outputStream:
        output.write(outputStream)

    # input("Press Enter to continue...")





