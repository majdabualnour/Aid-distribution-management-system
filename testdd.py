import subprocess
import os

# Define your Arabic text (replace with your actual Arabic text)

def dd(arabic_text):

   

    # Define the filename for the text file
    file_name = 'arabic_text.txt'

    # Write Arabic text to the text file with UTF-8 encoding
    with open(file_name, 'w', encoding='utf-8') as file:
        file.write(arabic_text)

    # Print the file using the lpr command (ensure lpr command is correct for your system)
    lpr_command = ['/usr/bin/lpr', '-P', 'SPRT-', file_name]  # Replace 'your_printer_name' with your actual printer name
    subprocess.run(lpr_command)

    # Optional: You can delete the file after printing if you don't need it anymore
    os.remove(file_name)

