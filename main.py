# Install PyPDF2  - pip install PyPDF2

import os
from SpecialConditionsClass import SpecialConditionsClass
from SplitBlockPdf import SplitBlockPdf

def readBlockAndCreateSibgleContractPdfs():
    # Read the block pdfs inside ./BlocksOfPdfs and extract single contract pdfs inside ./ExampleFolder
    blocksPath = "./BlocksOfPdfs"
    pdfsPath = "./SingleContractPdfs"
    # Iterate through the folder
    for fn in os.listdir(blocksPath):
        file_path = os.path.join(blocksPath, fn)

        # For each file - Check if it is a file (not a folder)
        if os.path.isfile(file_path):
            SplitBlockPdf(file_path, pdfsPath)


def readPdfsAndExtractCsv():
    # Define the relative folder path where the pdf files are
    relative_folder_path = './SingleContractPdfs'

    # Create a list with Special Conditions of ALL Contracts-Files
    project = SpecialConditionsClass(relative_folder_path)
    # project.extractToFile("SpecialConditions.csv")
    project.extractContractsWithCover("OnyContractsWithCover.csv")


if __name__ == "__main__":
    # Read the pdfs with multiple contracts
    # Create single contract pdfs.
    # readBlockAndCreateSibgleContractPdfs()

    # Read pdf files and extract csv with the results
    readPdfsAndExtractCsv()



