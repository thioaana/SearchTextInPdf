import PyPDF2

class SplitBlockPdf :

    def __init__(self, fn, pathToDest) :
        self._blockFileName = fn
        self._folderToSavePdfs = pathToDest
        self._blockText = []
        self._contractLength = []
        self._run()


    def _run(self):
        self._extractPdfsInTextMode()
        self._getContractLength()
        self._createMultiplePdfs()


    def _extractPdfsInTextMode(self):
        '''
        Reads the Block pdf file, ie the pdf with multiple contracts
        Converts it in text mode and save in the list of lists _blockText.
        Each element of the list contains a page. Each page is a list of rows.
        '''
        # Open the file as Read Binary
        pdfFileObj = open(self._blockFileName, 'rb')

        # Create a p000df reader object.
        pdfReader = PyPDF2.PdfReader(pdfFileObj)

        numPages = len(pdfReader.pages)

        for i in range(numPages):
            pageObj = pdfReader.pages[i]
            self._blockText.append(pageObj.extract_text().split("\n"))


    def _getContractLength(self):
        # Loop per page (element) of the _blockText
        for idp, page in enumerate(self._blockText):

            # Check first row whether it is equal with "ΑΣΦΑΛΙΣΤΗΡΙΟ ΠΕΡΙΟΥΣΙΑΣ"
            # In this case, this page is the first page of the contract
            if page[0] in ["ΑΣΦΑΛΙΣΤΗΡΙΟ ΠΕΡΙΟΥΣΙΑΣ", "ΚΟΙΝΟ ΣΥΝΑΣΦΑΛΙΣΤΗΡΙΟ ΠΕΡΙΟΥΣΙΑΣ"] :
                # Get the contract number
                pv = page[1].split('/')
                policy = pv[0].split(" ")[-1]

                # Append _firstPagePerContract with a tuple
                # The tuple consists of Contract No and the Number of the page
                self._contractLength.append([policy, idp, len(self._blockText) - 1])

        for idc in range(len(self._contractLength)-1):
            self._contractLength[idc][2] = self._contractLength[idc + 1][1] - 1

        self.printContractNumbers()


    def _createMultiplePdfs(self):
        with open(self._blockFileName, "rb") as inFn:
            pdfReader = PyPDF2.PdfReader(inFn)

            # For each contract in self._contractLength
            for idc, contract in enumerate(self._contractLength) :
                # Check whether the current contract is repeated in the next contracts and BREAK
                if idc < len(self._contractLength) - 1 :
                    if self._contractLength[idc] in [c[0] for c in self._contractLength][idc + 1 :] :
                        break

                pdfWriter = PyPDF2.PdfWriter()

                for p in range(contract[1], contract[2] + 1) :
                    pdfWriter.add_page(pdfReader.pages[p])

                # Save the selected pages to a new PDF
                with open(f"{self._folderToSavePdfs}/{contract[0]}.pdf", "wb") as outFn :
                    pdfWriter.write(outFn)


    def printBlockText(self, fromPage=1, toPage=0):
        if toPage == 0 :
            toPage = len(self._blockText)

        for no, p in enumerate(self._blockText[fromPage - 1: toPage]) :
            print(f"Page : {no + 1}")

            for  r in p :
                print(r)


    def printContractNumbers(self):
        for p in self._contractLength:
            print(f"Contract : {p[0]}\tPage : [{p[1]}, {p[2]}]")
