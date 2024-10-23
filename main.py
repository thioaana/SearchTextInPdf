# Install PyPDF2  - pip install PyPDF2

import os
from SpecialConditionsClass import SpecialConditionsClass

if __name__ == "__main__":

    # Define the relative folder path where the pdf files are
    relative_folder_path = './pdfFiles'

    # Create a list with Special Conditions of ALL Contracts-Files
    project = SpecialConditionsClass(relative_folder_path)
    project.extractToFile("SpecialConditions.csv")
    # project.printAllSC()

