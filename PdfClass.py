import PyPDF2

class PdfClass :
    _phrasesToSearch = ["ΚΑΠΝΟΣ"]

    def __init__(self, fn) :
        self._pdfFileName = fn      # Name of the pdf file
        self._text = []             # List of lists. Each list is a page. Each element is a row of the page
        self._pdfReader = None      # The reader object 

        
    def _readPdfExtractText(self):
        # Open the file as Read Binary
        pdfFileObj = open(self._pdfFileName, 'rb')

        # Create a pdf reader object.
        self._pdfReader = PyPDF2.PdfReader(pdfFileObj)

        numPages = len(self._pdfReader.pages)

        # Get each page, transform it and append _text list
        for i in range(numPages):
            pageObj = self._pdfReader.pages[i]
            self._text.append(pageObj.extract_text().split("\n"))


    def searchForPhrases(self):
        print(self._text[1])
        for page in self._text[1:] :
            # print(page)
            for row in range(len(page)) :
                print(page[row])
                break
            break
                # print(type(row), " - ", row)
                # break
                # if row.find("Φ") :
                #     print(row)
                #     break
        

    
    def getNumOfPages(self):
        # Print the number of pages of the file
        return len(self._text)
    

    def getPage(self, i):
        if i < len(self._text) :
            return self._text[i]
        else :
            return None