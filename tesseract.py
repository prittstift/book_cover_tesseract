from PIL import Image
import pytesseract

# If you don't have tesseract executable in your PATH, include the following:
pytesseract.pytesseract.tesseract_cmd = r'Link to Tesseract'

document_image = 'test_image.jpg'

# Simple image to string
# print(pytesseract.image_to_string(Image.open(document_image)))

# French text image to string
print(pytesseract.image_to_string(Image.open(document_image)))

# In order to bypass the image conversions of pytesseract, just use relative or absolute image path
# NOTE: In this case you should provide tesseract supported images or tesseract will return error
# print(pytesseract.image_to_string(Image.open(document_image)))

# Batch processing with a single file containing the list of multiple image file paths
# print(pytesseract.image_to_string('images.txt'))

# Get bounding box estimates
print(pytesseract.image_to_boxes(Image.open(document_image)))

# Get verbose data including boxes, confidences, line and page numbers
# print(pytesseract.image_to_data(Image.open(document_image)))

# Get information about orientation and script detection
# print(pytesseract.image_to_osd(Image.open(document_image)))

# Get a searchable PDF
# pdf = pytesseract.image_to_pdf_or_hocr(document_image, extension='pdf')

# Get HOCR output
# hocr = pytesseract.image_to_pdf_or_hocr(document_image, extension='hocr')
