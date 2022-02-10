class flxp():
    """ Klasse für den Export von Werten in eine CSV Datei
        Class for export data into csv file

    flexport requires the following parameters to create the object:

        path        --> e.g. C:\target-export-folder-name        don´t close the path with an \ at the end
        filename    --> e.g. testfilename                        don´t use a extension
        extension   --> e.g. txt or csv                          don´t use a . (dot) in the extension variable
        separator   --> e.g. ; (semicolon)

    The methode .test only prints the complete path and filename in the shell and prints the content of variable data
    Variable data is to send into the .test methode and must be a list e.g. "Value","Value2","Value3"
    There is no limit to the items in the list. flexport will process all items of a list
    The values in the list must be string only.
    Variable wp ist to choose w = overwrite existing file or a = append record to existing file
    flexport.test(data,wp)

    Variable wp ist to choose w = overwrite existing file or a = append record to existing file

    The methode .flexport is the main methode to export data into a file
    Modul .flexport expects a variable data which is a list with strings
    use flexport.export(data,wp)

    The modul file flexport_modul.py must be located in the project folder.

    Example Use:

    import flexport_modul as flp
    pfad = r"Z:\Python Projekte Code\tests"
    fp = flp.flxp(pfad, "testdatei", "txt",";")
    fp.flexport(["1234","4545","4545"], "a")


    """
    
    def __init__(self, path, filename, extension, separator):
        self.path = path + "\\"
        self.filename = filename
        self.extension = extension
        self.separator = separator

    def test(self, data,wp):
        print("Test")
        print("Export into "+self.path + self.filename + "." + self.extension)
        print("Write modus = "+wp)
        print("Separator: " + self.separator)
        print("")
        dataline = self.separator.join(data)
        print(datalin)

    def flexport(self,data,wp):
        try:
            file = open(self.path + self.filename + "." + self.extension,"r")
            file.close()
            file = open(self.path + self.filename + "." + self.extension,wp)
            dataline = self.separator.join(data)
            file.write("\n"+dataline)
            file.close()
  
        except:
            file = open(self.path + self.filename + "." + self.extension,wp)
            dataline = self.separator.join(data)
            file.write(dataline)
            file.close()