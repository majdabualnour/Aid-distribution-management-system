import subprocess
from PIL import Image, ImageDraw, ImageFont
from datetime import datetime
output_path = "print_image.png"
logo_path = "logo.png"
def create_print_image( text,  code, id, ee):
    text = str(text)
    # Load the logo image and resize it to be bigger
    logo = Image.open(logo_path)
    icon_size = 200  # Increase size of the icon (in pixels)
    logo_resized = logo.resize((icon_size, icon_size))

    # Create a blank image with white background
    image_width = 80 * 10  # 80mm width in pixels
    font_size = 30  # Decrease font size for the text

    # Using a common TrueType font path (modify if needed)
    common_fonts = [
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
        "/usr/share/fonts/truetype/freefont/FreeSansBold.ttf",
        "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"
    ]
    
    # Find an available font
    for font_path in common_fonts:
        try:
            font = ImageFont.truetype(font_path, font_size)
            break
        except IOError:
            continue
    else:
        raise IOError("No valid font found.")

    text_height = font.getsize(text)[1]
    border_padding = 10  # Increase this value to add more white borders at the top and bottom
    image_height = max(icon_size, text_height + 30) + 8 * border_padding  # Adjust height to fit text and icon with more padding

    image = Image.new("L", (image_width, 1000), "white")
    
    # Paste the resized logo as an icon at the edge of the image
    image.paste(logo_resized, (0, (image_height - icon_size) // 3))

    # Draw the text onto the image centered
    draw = ImageDraw.Draw(image)
    text_width = draw.textsize(text, font=font)[0]
    
    text_position = (40 , (image_height - text_height) // 2+100) 
    text_position6 = (40 , (image_height - text_height) // 2+140) 
     # Adjust position with more padding
    text_position1 = ( 10, (image_height - text_height) // 2 +300)  # Adjust position with more padding
    text_position3= (10, (image_height - text_height) // 2 +200)    # Adjust position with more padding
    text_position2= (10, (image_height - text_height) // 2 +400) 

    pp =  str(datetime.now()).split(' ')
    draw.text(text_position, pp[0], fill="black", font=font , font_size= 5)
    draw.text(text_position6, pp[1], fill="black", font=font , font_size= 5)
    for font_path in common_fonts:
        try:
            font = ImageFont.truetype(font_path, 40)
            break
        except IOError:
            continue
    else:
        raise IOError("No valid font found.")

    draw.text(text_position2, str(text), fill="black", font=font)
    for font_path in common_fonts:
        try:
            font = ImageFont.truetype(font_path, 60)
            break
        except IOError:
            continue
    else:
        raise IOError("No valid font found.")
    draw.text(text_position3, str(code), fill="black", font=font)
    # font = ImageFont.truetype('fre3of9x.ttf',100)
    draw.text(text_position1, f'{str(id)}', fill="black", font=font)

    if ee:
        text_positionerer = ( 10, (image_height - text_height) // 2 +450)  # Adjust position with more padding

        draw.text(text_positionerer, str(ee), fill="black", font=font)
    # Rotate the image 90 degrees counterclockwise to make it vertical
    image = image.rotate(90, expand=True)

    # Save the image
    image.save(output_path)
    subprocess.run(['lp', '-o', 'landscape', output_path], check=True)

