# Install PyPDF2  - pip install PyPDF2

import os
from PdfClass import PdfClass

if __name__ == "__main__":
    # Read pdf file name
    # As a start the file name is imported directy to a variable
    # fn = "2045883137-14.pdf"
    # contract = PdfClass(fn)

    # Define the relative folder path
    relative_folder_path = './pdfFiles'

    # Iterate through the folder
    for file_name in os.listdir(relative_folder_path):
        file_path = os.path.join(relative_folder_path, file_name)
        
        # Check if it's a file (not a directory)
        if os.path.isfile(file_path):
            print(file_name)
            contract = PdfClass(file_path)
            
    print(PdfClass._conclusion)




  

