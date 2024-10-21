# Install PyPDF2  - pip install PyPDF2

import PyPDF2
from PdfClass import PdfClass

if __name__ == "__main__":
    # Read pdf file name
    # As a start the file name is imported directy to a variable
    fn = "2045883137-14.pdf"
    contract = PdfClass(fn)
    contract._readPdfExtractText()

    contract.searchForPhrases()


  

