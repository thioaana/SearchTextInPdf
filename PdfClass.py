import PyPDF2

class PdfClass :
    '''
    This class handles the text of a pdf and extracts conclusions
    '''

    _conclusion = {}    # Will be in the form {contract: _phrasesToSearch}


    def __init__(self, fn) :
        self._pdfFileName = fn      # Name of the pdf file
        self._text = []             # List of lists. Each list is a page. Each element is a row of the page
        self._pdfReader = None      # The reader object 
        self._phrasesToSearch = {"ΚΑΠΝΟΣ": [],
                                "ΟΡΟΣ ΠΡΟΝΟΙΑΣ": [],
                                "ΑΥΤΟΜΑΤΗ ΑΝΑΣΥΣΤΑΣΗ": [],
                                "ΝΕΟΑΠΟΚΤΗΘΕΝΤΑ": [],
                                "ΟΡΟΣ 72": [],
                                "ΚΑΤΑ ΤΗΝ ΔΙΑΡΚΕΙΑ ΕΡΓΑΣΙΩΝ": [],
                                "ΖΗΜΙΕΣ ΚΛΕΠΤΗ ΣΤΟ ΚΤΙΡΙΟ": [],
                                "ΑΞΙΑ ΚΑΙΝΟΥΡΓΙΟΥ": []}

        self._run()

    def _run(self):
        '''
        The logic of the project for a specific pdf file
        '''
        self._readPdfExtractText()
        self._searchForPhrases()
        self._fillCoclusion()



    def _readPdfExtractText(self):
        '''
        This fuction takes a pdf file name and extracts the conent of the file in a list of lists 
        '''
        # Open the file as Read Binary
        pdfFileObj = open(self._pdfFileName, 'rb')

        # Create a p000df reader object.
        self._pdfReader = PyPDF2.PdfReader(pdfFileObj)

        numPages = len(self._pdfReader.pages)

        # Get each page, transform it and append _text list
        for i in range(numPages):
            pageObj = self._pdfReader.pages[i]
            self._text.append(pageObj.extract_text().split("\n"))


    def _searchForPhrases(self):
        '''
        This function searches in the text list for spacific phrases included in _phrasesForSearch.
        Saves the reasult in the _phrasesForSearch dict.
        '''
        for key in self._phrasesToSearch :
            for idp, page in enumerate(self._text[:5]) :
                for idr, row in enumerate(page) :
                    if row.find(key) >= 0:
                        self._phrasesToSearch[key].append(f"{idr}/{idp}-->{row}")
                        # print(f"{idr}/{idp}-->{row}")
        # print(self._phrasesToSearch)


    def _fillCoclusion(self):
        def _getContractNum() :
            for r in self._text[0]:
                if r.find("ΑΡΙΘΜΟΣ ΑΣΦΑΛΙΣΤΗΡΙΟΥ") >= 0 :
                    pv = r.split(' ')[3]
                    return (pv.split('/')[0], pv.split('/')[1])
        
        (c, v) = _getContractNum()
        self._conclusion[c] = {"Version": v, "Justification": self._phrasesToSearch}
        
    

    def getNumOfPages(self):
        # Print the number of pages of the file
        return len(self._text)
    

    def getPage(self, i):
        if i < len(self._text) :
            return self._text[i]
        else :
            return None