import PyPDF2

class PdfClass :
    '''
    This class handles the text of a pdf and extracts conclusions
    Variable _conclusion is static.
    It keeps the search results from all files
    '''

    def __init__(self, fn) :
        self._pdfFileName = fn      # Name of the pdf file
        self._text = []             # List of lists. Each list is a page. Each element is a row of the page
        self._pdfReader = None      # The reader object 
        self._searchFor = {"KAPNOS": {"Search Cover" : "- Kapnos", "Cover Found": [], "Search Wording": ["ΚΑΠΝΟΣ"], "Wording Found": []},
                           "PRONOIA": {"Search Cover" : "- Oros Pronoias", "Cover Found": [], "Search Wording": ["ΟΡΟΣ ΠΡΟΝΟΙΑΣ"], "Wording Found": []},
                           "ANASYSTASH": {"Search Cover" : "- Aytomath Anasystash", "Cover Found": [], "Search Wording": ["ΑΥΤΟΜΑΤΗ ΑΝΑΣΥΣΤΑΣΗ"], "Wording Found": []},
                           "NEOAPOKTHUENTA": {"Search Cover" : "- Neoapokthuenta", "Cover Found": [], "Search Wording": ["ΝΕΟΑΠΟΚΤΗΘΕΝΤΑ"], "Wording Found": []},
                           "72": {"Search Cover" : "- Oros 72 Vrvn", "Cover Found": [], "Search Wording": ["ΟΡΟΣ 72"], "Wording Found": []},
                           "KATA TH DIARKEIA": {"Search Cover" : "- kATA TH DIARKEIA", "Cover Found": [], "Search Wording": ["ΚΑΤΑ ΤΗΝ ΔΙΑΡΚΕΙΑ ΕΡΓΑΣΙΩΝ"], "Wording Found": []},
                           "ZHMIES KLEPTH": {"Search Cover" : "- Zhmies Klepth", "Cover Found": [], "Search Wording": ["ΖΗΜΙΕΣ ΚΛΕΠΤΗ ΣΤΟ ΚΤΙΡΙΟ"], "Wording Found": []},
                           "AJIA KAINOYRGIOY": {"Search Cover" : "- Ajia Kainoyrgioy", "Cover Found": [], "Search Wording": ["ΑΞΙΑ ΚΑΙΝΟΥΡΓΙΟΥ"], "Wording Found": []},}
        self._conclusion = {}    # Will be in the form {contract: _phrasesToSearch}


    def run(self):
        '''
        The logic of the project for a specific pdf file
        '''
        self._readPdfExtractText()
        self._searchForPhrases()
        self._fillCoclusion()
        return self._conclusion


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
        for k, v in self._searchFor.items() :
            for idp, page in enumerate(self._text) :
                for idr, row in enumerate(page) :
                    # Search for wording in the row
                    for lst in v["Search Wording"] :
                        if row.find(lst) >= 0:
                            self._searchFor[k]["Wording Found"].append(f"{idr + 1}/{idp + 1}-->{row}")

                    # Search for cover in the row
                    if row.find(v["Search Cover"]) >= 0:
                        self._searchFor[k]["Cover Found"].append(f"{idr + 1}/{idp + 1}-->{row}")


    def _fillCoclusion(self):
        def _getContractNum() :
            for r in self._text[0]:
                if r.find("ΑΡΙΘΜΟΣ ΑΣΦΑΛΙΣΤΗΡΙΟΥ") >= 0 :
                    pv = r.split('/')
                    p = pv[0].split(" ")[-1]
                    v = pv[1].split(" ")[0]
                    return (p, v)
        
        (p, v) = _getContractNum()
        self._conclusion["Vertran"] = p
        self._conclusion["Version"] = v

        self._conclusion["Cover Found"] = {k: v["Cover Found"] for k, v in self._searchFor.items()}
        self._conclusion["Wordings Found"] = {k: v["Wording Found"] for k, v in self._searchFor.items()}

    def getNumOfPages(self):
        # Print the number of pages of the file
        return len(self._text)
    

    def getPage(self, i):
        if i < len(self._text) :
            return self._text[i]
        else :
            return None