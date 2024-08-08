from PIL import Image, ImageDraw, ImageFont

def create_barcode(text, font_path, output_file):
    # Load the font
    font = ImageFont.truetype(font_path, 40)

    # Create an image with white background
    width, height = font.getsize(text)
    img = Image.new('1', (width, height), 1)  # 1-bit pixels, black and white
    draw = ImageDraw.Draw(img)

    # Draw the text (barcode)
    draw.text((0, 0), text, font=font)

    # Save the image
    img.save(output_file)

# Example usage
barcode_text = '*123456789012*'  # Code 39 barcode text (start and end with *)
font_path = 'fre3of9x.ttf'  # Replace with the path to your barcode font
create_barcode(barcode_text, font_path, 'barcode.png')
