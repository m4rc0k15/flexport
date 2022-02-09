class flxp():
    """ Klasse für den Export von Werten in eine CSV Datei
        Class for export data into csv file

    flexport requires the following parameters:

        path        --> e.g. C:\target-export-folder-name        don´t close the path with an \ at the end
        filename    --> e.g. testfilename                        don´t use a extension
        extension   --> e.g. txt or csv                          don´t use a . (dot) in the extension variable

    The methode .test only prints the complete path and filename in the shell and prints the content of variable data
    Variable data is to send into the .test methode and must be a list e.g. "Value","Value2","Value3"
    There is no limit to the items in the list. flexport will process all items of a list
    The values in the list must be string only.
    Variable wp ist to choose w = overwrite existing file or a = append record to existing file
    flexport.test(data,wp)

    Variable wp ist to choose w = overwrite existing file or a = append record to existing file

    The methode .export is the main methode to use
    Modul .export expects a variable data too with a list of strings
    flexport.export(data,wp)

    """
    
    def __init__(self, path, filename, extension):
        self.path = path + "\\"
        self.filename = filename
        self.extension = extension

    def test(self, data,wp):
        print("Test")
        print("Export into "+self.path + self.filename + "." + self.extension)
        print("Write modus = "+wp)
        print("")
        print(data)

    def flexport(self,data,wp):
        try:
            file = open(self.path + self.filename + "." + self.extension,"r")
            file.close()
            file = open(self.path + self.filename + "." + self.extension,wp)
            dataline = ";".join(data)
            file.write("\n"+dataline)
            file.close()
  
        except:
            file = open(self.path + self.filename + "." + self.extension,wp)
            dataline = ";".join(data)
            file.write(dataline)
            file.close()