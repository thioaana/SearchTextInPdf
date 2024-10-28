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
        self._searchFor = {"Φ1775": {"Search Cover" : "-Καπνός", "Cover Found": [],
                                     "Search Wording": ["ΚΑΠΝΟΣ"], "Wording Found": [],
                                     "Search Term": "Ειδικός όρος 12 ", "Term Found": []},
                           "Φ1776": {"Search Cover": "-Έξοδα φύλαξης", "Cover Found": [],
                                     "Search Wording": ["ΕΞΟΔΑ ΦΥΛΑΞΗΣ"], "Wording Found": [],
                                     "Search Term": "Ειδκός όρος 147", "Term Found": []},
                           "Φ1770": {"Search Cover": "-Έξοδα μεταστέγασης", "Cover Found": [],
                                     "Search Wording": ["ΕΞΟΔΑ μεταστεγασης"], "Wording Found": [],
                                     "Search Term": "Ειδικός όρος 124", "Term Found": []},
                           "Φ1734": {"Search Cover": "-Έξοδα άντλησης", "Cover Found": [],
                                     "Search Wording": ["ΕΞΟΔΑ ΑΝΤΛΗΣΗΣ"], "Wording Found": [],
                                     "Search Term": "Ειδικός όρος 125", "Term Found": []},
                           "Φ1717": {"Search Cover": "-Βραχυκύκλωμα χωρίς εστία φωτιάς", "Cover Found": [],
                                     "Search Wording": ["ΒΡΑΧΥΚΥΚΛΩΜΑ ΧΩΡΙΣ ΕΣΤΙΑ"], "Wording Found": [],
                                     "Search Term": "Ειδικός όρος 121", "Term Found": []},
                           "Φ1737": {"Search Cover": "-Έξοδα διερευνητικών", "Cover Found": [],
                                     "Search Wording": ["ΕΞΟΔΑ ΔΙΕΡΕΥΝΗΤΙΚΩΝ"], "Wording Found": [],
                                     "Search Term": "Ειδικός όρος 126", "Term Found": []},
                           "Φ1716": {"Search Cover": "-Ίδιες ζημιές λέβητα", "Cover Found": [],
                                     "Search Wording": ["ΙΔΙΕΣ ΖΗΜΙΕΣ ΛΕΒΗΤΑ"], "Wording Found": [],
                                     "Search Term": "Ειδικός όρος 93", "Term Found": []},
                           "Φ2210": {"Search Cover": "-Αστική ευθύνη συνεπεία καλυπτομένου", "Cover Found": [],
                                     "Search Wording": ["ΑΣΤΙΚΗ ΕΥΘΥΝΗ ΣΥΝΕΠΕΙΑ ΚΑΛΥΠΤΟΜΕΝΟΥ"], "Wording Found": [],
                                     "Search Term": "Ειδικός όρος 141", "Term Found": []},
                           "Φ1728": {"Search Cover": "-Έξοδα ελαχιστοποίησης", "Cover Found": [],
                                     "Search Wording": ["ΕΞΟΔΑ ΕΛΑΧΙΣΤΟΠΟΙΗΣΗΣ"], "Wording Found": [],
                                     "Search Term": "Ειδικός όρος 127", "Term Found": []},
                           "Φ1754": {"Search Cover": "-Αλλοίωση εμπορευμάτων", "Cover Found": [],
                                     "Search Wording": ["ΑΛΛΟΙΩΣΗ ΕΜΠΟΡΕΥΜΑΤΩΝ"], "Wording Found": [],
                                     "Search Term": "Ειδικός όρος XXXXX", "Term Found": []},
                           "Φ1757": {"Search Cover" : "-Oros Pronoias", "Cover Found": [],
                                     "Search Wording": ["ΟΡΟΣ ΠΡΟΝΟΙΑΣ"], "Wording Found": [],
                                     "Search Term": "Ειδικός όρος XXXXX", "Term Found": []},
                           "ANASYSTASH": {"Search Cover" : "-Aytomath Anasystash", "Cover Found": [],
                                          "Search Wording": ["ΑΥΤΟΜΑΤΗ ΑΝΑΣΥΣΤΑΣΗ"], "Wording Found": [],
                                          "Search Term": "Ειδικός όρος XXXXX", "Term Found": []},
                           "NEOAPOKTHUENTA": {"Search Cover" : "-Neoapokthuenta", "Cover Found": [],
                                              "Search Wording": ["ΝΕΟΑΠΟΚΤΗΘΕΝΤΑ"], "Wording Found": [],
                                              "Search Term": "Ειδικός όρος XXXXX", "Term Found": []},
                           "72": {"Search Cover" : "-Oros 72 Vrvn", "Cover Found": [],
                                  "Search Wording": ["ΟΡΟΣ 72"], "Wording Found": [],
                                  "Search Term": "Ειδικός όρος XXXXX", "Term Found": []},
                           "KATA TH DIARKEIA": {"Search Cover" : "-kATA TH DIARKEIA", "Cover Found": [],
                                                "Search Wording": ["ΚΑΤΑ ΤΗΝ ΔΙΑΡΚΕΙΑ ΕΡΓΑΣΙΩΝ"], "Wording Found": [],
                                                "Search Term": "Ειδικός όρος XXXXX", "Term Found": []},
                           "Φ1813": {"Search Cover" : "-Ζημιές", "Cover Found": [],
                                     "Search Wording": ["ΖΗΜΙΕΣ ΚΛΕΠΤΗ ΣΤΟ ΚΤΙΡΙΟ"], "Wording Found": [],
                                     "Search Term": "Ειδικός όρος 112", "Term Found": []},
                           "AJIA KAINOYRGIOY": {"Search Cover" : "-Ajia Kainoyrgioy", "Cover Found": [],
                                                "Search Wording": ["ΑΞΙΑ ΚΑΙΝΟΥΡΓΙΟΥ"], "Wording Found": [],
                                                "Search Term": "Ειδικός όρος 42 ", "Term Found": []},
                           }
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
                    termFound = False
                    # Search for cover in the row
                    if row.find(v["Search Cover"]) >= 0:
                        self._searchFor[k]["Cover Found"].append(f"{idr + 1}/{idp + 1}-->{row}")

                    # Search for wording in the row
                    for lst in v["Search Wording"] :
                        if row.find(lst) >= 0:
                            if row.find(v["Search Term"]) >= 0 :
                                self._searchFor[k]["Term Found"].append(f"{idr + 1}/{idp + 1}-->{row}")
                                termFound = True
                            else :
                                self._searchFor[k]["Wording Found"].append(f"{idr + 1}/{idp + 1}-->{row}")

                    # Search for term in the row
                    if row.find(v["Search Term"]) >= 0 and not termFound:
                        self._searchFor[k]["Term Found"].append(f"{idr + 1}/{idp + 1}-->{row}")


    def _fillCoclusion(self):
        def _getContractNum() :
            for r in self._text[0]:
                if r.find("ΑΡΙΘΜΟΣ ΑΣΦΑΛΙΣΤΗΡΙΟΥ") >= 0 :
                    pv = r.split('/')
                    p = pv[0].split(" ")[-1]
                    v = pv[1].split(" ")[0]
                    return (p, v)

        def _getSI():
            for r in self._text[0]:
                if r.find("ΣΥΝΟΛΙΚΟ ΑΣΦΑΛΙΣΤΙΚΟ ΠΟΣΟ") >= 0 :
                    si = r.split(' ')
                    return si[-1]

        def _getInsured():
            for r in self._text[0]:
                if r.find("ΛΗΠΤΗΣ ΤΗΣ ΑΣΦΑΛΙΣΗΣ") >= 0 :
                    indexAFM = r.find("Α.Φ.Μ")
                    return r[22:indexAFM]

        
        (p, v) = _getContractNum()
        self._conclusion["Vertran"] = p
        self._conclusion["Version"] = v
        self._conclusion["Insured"] = _getInsured()
        self._conclusion["SI"] = _getSI()

        self._conclusion["Cover Found"] = {k: v["Cover Found"] for k, v in self._searchFor.items()}
        self._conclusion["Wordings Found"] = {k: v["Wording Found"] for k, v in self._searchFor.items()}
        self._conclusion["Term Found"] = {k: v["Term Found"] for k, v in self._searchFor.items()}

        # print(self._conclusion)


    def getNumOfPages(self):
        # Print the number of pages of the file
        return len(self._text)
    

    def getPage(self, i):
        if i < len(self._text) :
            return self._text[i]
        else :
            return None