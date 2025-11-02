from PIL import Image
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os

# Define the directory containing the images
image_folder = "./images"  # Update this path to your images folder
output_pdf = "screentime-collection.pdf"

# Create a PDF canvas
pdf = canvas.Canvas(output_pdf, pagesize=letter)

# Get a list of all image files in the folder
images = [f for f in os.listdir(image_folder) if f.lower().endswith(('png', 'jpg', 'jpeg', 'gif', 'bmp'))]

# Loop through images and add each one to the PDF
for image_name in images:
    image_path = os.path.join(image_folder, image_name)
    
    # Open the image to get its size
    img = Image.open(image_path)
    img_width, img_height = img.size
    
    # Adjust image size to fit within the page (keeping aspect ratio)
    page_width, page_height = letter
    aspect_ratio = img_width / img_height
    if img_width > img_height:
        img_width = page_width
        img_height = page_width / aspect_ratio
    else:
        img_height = page_height
        img_width = page_height * aspect_ratio
    
    # Center the image on the page
    x_offset = (page_width - img_width) / 2
    y_offset = (page_height - img_height) / 2
    
    # Draw the image on the PDF
    pdf.drawImage(image_path, x_offset, y_offset, img_width, img_height)
    
    # Add a new page for the next image
    pdf.showPage()

# Save the PDF
pdf.save()
