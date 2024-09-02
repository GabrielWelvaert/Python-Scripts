import os
from PIL import Image

# Set the desired width and height
w, h = 720, 404# Change these values as needed

# Get the current directory
current_dir = os.getcwd()

# Iterate over all files in the current directory
for filename in os.listdir(current_dir):
    if filename.endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):  # Add more formats if needed
        try:
            # Open an image file
            with Image.open(filename) as img:
                # Resize the image using LANCZOS filter
                img_resized = img.resize((w, h), Image.LANCZOS)
                
                # Save the image with the same name, overwriting the original
                img_resized.save(filename)
                
                print(f"Resized and saved: {filename}")
        except Exception as e:
            print(f"Failed to resize {filename}: {e}")

print("All images have been resized.")
