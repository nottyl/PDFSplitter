import os
from PyPDF2 import PdfReader, PdfWriter

# Open the input PDF file
input_file_path = 'path/to/pdf'
input_pdf = PdfReader(open(input_file_path, 'rb'))

# Create a new directory to store the output PDF files
output_dir_path = 'path/to/output'
if not os.path.exists(output_dir_path):
    os.makedirs(output_dir_path)

# Loop through each page in the input PDF file and save it as a separate PDF file
for i in range(len(input_pdf.pages)):
    # Create a new PDF writer
    output_pdf = PdfWriter()

    # Add the current page to the new PDF writer
    output_pdf.add_page(input_pdf.pages[i])

    # Save the new PDF file with the page number as the filename
    output_file_path = os.path.join(output_dir_path, f'page_{i+1}.pdf')
    with open(output_file_path, 'wb') as output_file:
        output_pdf.write(output_file)
