# Image Processing: Use PIL to invert the colors of an image.

from PIL import Image, ImageOps

# Open an image
image = Image.open("input.jpg")  # Replace with your image file

# Invert the image colors
inverted_image = ImageOps.invert(image.convert("RGB"))  # Convert to RGB before inverting

# Save or show the result
inverted_image.show()  # Display the image
inverted_image.save("output.jpg")  # Save the inverted image