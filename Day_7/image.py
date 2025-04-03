# Image Processing: Use PIL to invert the colors of an image.

from PIL import Image, ImageOps

# Open an image
image = Image.open("input.jpg")  # Replace with your image file


inverted_image = ImageOps.invert(image.convert("RGB")) 

inverted_image.show()  
inverted_image.save("output.jpg")  # Save the inverted image