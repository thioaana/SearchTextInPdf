import os
from PdfClass import PdfClass


class SpecialConditionsClass :

    def __init__(self, relative_folder_path):

        # This list keeps the Special Conditions af ALL pdf files in the requested folder
        self._specialConditions = []

        # Iterate through the folder
        for file_name in os.listdir(relative_folder_path):
            file_path = os.path.join(relative_folder_path, file_name)

            # For each file - Check if it is a file (not a directory)
            if os.path.isfile(file_path):
                # Initialize and get the Special Conditions of the specific Contract-file
                contract = PdfClass(file_path)
                sC = contract.run()

                # Append the list with the specific special condition.
                self._specialConditions.append(sC)


    def extractToFile(self, csvFN):
        dict0 = self._specialConditions[0]
        print(dict0)
        covers = [k for k in dict0["Cover Found"].keys()]

        with open(csvFN, 'w') as f:
            header = f"Συμβόλαιο;Version;Λήπτης της Ασφάλισης;Κεφάλαιο;Καπνός;special cond;attachment;Έξοδα φύλαξης;" \
                     f"special cond;attachment;Έξοδα μεταστέγασης;special cond;attachment;Έξοδα άντλησης;special cond;attachment;" \
                     f"Βραχυκύκλωμα χωρίς;special cond;attachment;Έξοδα διερευνητικών;special cond;attachment;" \
                     f"Ίδιες ζημιές λέβητα;special cond;attachment;Αστική;special cond;attachment;Έξοδα ελαχιστοποίησης;special cond;attachment;" \
                     f"Αλλοίωση;special cond;attachment;Πρόνοιας;special cond;attachment;Ανασύσταση;special cond;attachment;" \
                     f"Νεοαποκτηθέντα;special cond;attachment;72 ωρών;special cond;attachment;Κατά τη διάρκεια;special cond;attachment;Ζημιές κλέφτη;special cond;attachment;Καινούργιου\n"
            f.write(header)

            for d in self._specialConditions:
                p = d["Vertran"]
                v = d["Version"]
                si = d["SI"]
                insured = d["Insured"]
                record = f"{p};{v};{insured};{si}"

                for cover in covers:
                    record += ";" + ", ".join(d["Cover Found"][cover])
                    record += ";" + ", ".join(d["Wordings Found"][cover])
                    record += ";" + ", ".join(d["Term Found"][cover])
                    f.write
                record += "\n"
                f.write(record)



    def extractContractsWithCover(self, csvFN):
        def _checkCoverListIsEmpty(coversFound):
            # Check if list of cover values is totally empty
            lst = [c for c in coversFound.values()]
            return all(len(subLst) == 0 for subLst in lst)
            # print("Covers : ", lst)
            # print("It is empty : ", all(len(subLst) == 0 for subLst in lst))

        dict0 = self._specialConditions[0]
        covers = [k for k in dict0["Cover Found"].keys()]

        with open(csvFN, 'w') as f:
            header = f"Συμβόλαιο;Version;Λήπτης της Ασφάλισης;Κεφάλαιο;Καπνός;special cond;attachment;Έξοδα φύλαξης;" \
                     f"special cond;attachment;Έξοδα μεταστέγασης;special cond;attachment;Έξοδα άντλησης;special cond;attachment;" \
                     f"Βραχυκύκλωμα χωρίς;special cond;attachment;Έξοδα διερευνητικών;special cond;attachment;" \
                     f"Ίδιες ζημιές λέβητα;special cond;attachment;Αστική;special cond;attachment;Έξοδα ελαχιστοποίησης;special cond;attachment;" \
                     f"Αλλοίωση;special cond;attachment;Πρόνοιας;special cond;attachment;Ανασύσταση;special cond;attachment;" \
                     f"Νεοαποκτηθέντα;special cond;attachment;72 ωρών;special cond;attachment;Κατά τη διάρκεια;special cond;attachment;Ζημιές κλέφτη;special cond;attachment;Καινούργιου\n"
            f.write(header)

            for d in self._specialConditions:
                emptyOfCovers = _checkCoverListIsEmpty(d["Cover Found"])
                if emptyOfCovers :
                    continue
                # exit()

                p = d["Vertran"]
                v = d["Version"]
                si = d["SI"]
                insured = d["Insured"]
                record = f"{p};{v};{insured};{si}"

                for cover in covers:
                    record += ";" + ", ".join(d["Cover Found"][cover])
                    record += ";" + ", ".join(d["Wordings Found"][cover])
                    record += ";" + ", ".join(d["Term Found"][cover])
                    f.write
                record += "\n"
                f.write(record)

    def printAllSC(self):
        for iDict in self._specialConditions:
            for k, v in iDict.items():
                print(f"{k}: {v}")


