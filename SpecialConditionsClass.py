import os
from PdfClass import PdfClass


class SpecialConditionsClass :

    def __init__(self, relative_folder_path):

        # This list keeps the Special Conditions af ALL pdf files in the requested folder
        self._specialConditions = []

       # Iterate through the folder
        for file_name in os.listdir(relative_folder_path):
            file_path = os.path.join(relative_folder_path, file_name)
            
            # For each file
            # Check if it is a file (not a directory)
            if os.path.isfile(file_path):
                # Initialize and get the Special Conditions of the specific Contract-file
                contract = PdfClass(file_path)
                sC = contract.run()

                # Append the list with the specific special condition.
                self._specialConditions.append(sC)


    def extractToFile(self, csvFN):
        dict0 = self._specialConditions[0]
        covers = [k for k in dict0["Cover Found"].keys()]

        with open(csvFN, 'w') as f:
            for d in self._specialConditions:
                p = d["Vertran"]
                v = d["Version"]
                record = p + ";" + v
                for cover in covers:
                    # elt = d['Cover Found'][cover] +
                    for dj in d["Justification"]:
                    # # print(dj, d["Justification"][dj])
                        elt = d['Justification'][dj]
                        record += ";" + ", ".join(elt)
                        f.write
                # record += "\n"
                # f.write(record)


    def printAllSC(self):                
        for iDict in self._specialConditions:
            for k, v in iDict.items():
                print(f"{k}: {v}")


