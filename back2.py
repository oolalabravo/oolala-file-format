import tkinter as tk
from PIL import Image, ImageTk
import sys
import os

# Function to read pixel values from text file
def read_pixel_values(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    pixel_values_hex = []
    for line in lines:
        row = line.strip().split()
        pixel_values_hex.append(row[:-1])  # Remove the '#' character at the end
    return pixel_values_hex

# Function to convert pixel values to image and display in Tkinter window
def show_image_from_pixel_values(pixel_values):
    height = len(pixel_values)
    width = len(pixel_values[0])
    
    # Create a blank image
    im = Image.new('RGB', (width, height))
    pixels = im.load()
    
    # Convert hex values back to RGB and set pixels in the image
    for y in range(height):
        for x in range(width):
            hex_value = pixel_values[y][x]
            rgb_value = tuple(int(hex_value[i:i+2], 16) for i in (1, 3, 5))
            pixels[x, y] = rgb_value
    
    # Display image in Tkinter window
    root = tk.Tk()
    root.title("Image from Pixel Values")
    
    tk_image = ImageTk.PhotoImage(im)
    label = tk.Label(root, image=tk_image)
    label.pack()
    
    root.mainloop()

def main():
    if len(sys.argv) < 2:
        print("Usage: script.py <file_path>")
        return
    
    file_path = sys.argv[1]
    
    if file_path.lower().endswith('.oolala') and os.path.exists(file_path):
        # Read pixel values from the text file
        pixel_values = read_pixel_values(file_path)

        # Show image in Tkinter window
        show_image_from_pixel_values(pixel_values)
    else:
        print('File type not supported or file does not exist')

if __name__ == "__main__":
    main()
