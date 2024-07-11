from PIL import Image
from pathlib import Path

# Load the image
image_path = input('Enter image path:')
image_path2 = Path(image_path)
file_name = image_path2.stem  # This gives the filename without extension
output_file = f"F:/programs/jiff/{file_name}.oolala"

# Open the image
im = Image.open(image_path).convert("RGB")
width, height = im.size
pix = im.load()

# Prepare to store pixel values
pixel_values_hex = []

# Iterate over each pixel
for y in range(height):
    row_values = []
    for x in range(width):
        r, g, b = pix[x, y]
        hex_value = '#{0:02x}{1:02x}{2:02x}'.format(r, g, b)
        row_values.append(hex_value)
    pixel_values_hex.append(row_values)

# Save pixel values to a text file
with open(output_file, 'w') as file:
    for row in pixel_values_hex:
        file.write(' '.join(row) + '\n')

# Print confirmation message
print(f"Pixel values saved to: {output_file}")
