# flexport
flexible csv export modul for python

English Version:
----------------

The code flexport is a module for python to export simple data from a list into a target file.
Flexport excpects a list of string variables. Flexport requires following parameters to create the object.

path        --> e.g. C:\target-export-folder-name        don´t close the path with an \ at the end
filename    --> e.g. testfilename                        don´t use a extension
extension   --> e.g. txt or csv                          don´t use a . (dot) in the extension variable
separator   --> e.g. ; (semicolon)

The methode test only prints the complete path and filename in the shell and prints the content of variable data with separator.
Variable data is send into the test methode and must be a list e.g. "Value","Value2","Value3".
There is no limit to the items in the list. flexport will process all items of a list.
The values in the list must be string only.
Variable wp ist to choose w = overwrite existing file or a = append record to existing file.


The methode flexport is the main methode to export data into a file.
Modul .flexport expects a variable data which is a list with strings.

The FlexPort module must be located in the same folder as the actual project or must be imported specifying the correct path.

Example use:
------------

import flexport_modul as flp
pfad = r"Z:\Python Projekte Code\tests"
fp = flp.flxp(pfad, "testdatei", "txt",";")
fp.flexport(["1234","4545","4545"], "a")


-----------------------------------------------------------------------------------------------------------------------------
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
-----------------------------------------------------------------------------------------------------------------------------


German Version:
---------------

Das Modul flexport dient dem Export von Listen die ausschließlich String-Variablen beinhalten. Eine Liste kann als Datensatz in eine Datei exportiert werden.
Flexport verarbeitet einen Listendatensatz nach einander. Es ist möglich flexport flexibel durch Parameter anzupassen. Folgende Parameter sind bei der Erstellung
der Klasse notwendig:

path          -->     z.B. C:\ziel-ordner-name      nicht mit \ die Pfadangabe abschließen!
filename      -->     z.B. testDateiName            verwende keine Dateierweiterung!
extension     -->     z.B. txt oder csv             verwende keinen Punkt for der Dateiendung
separator     -->     z.B. ; (Semikolon)            jeses beliebige Zeichen und auch Zeichenketten sind möglich

Die Methode test gibt folgende Informationen auf der Shell wieder. Sie dient ausschließlich Testzwecken und erzeugt keine Export-Datei.
Der Aufruf der Methode text erwartet folgende Parameter die mit übergeben werden:

data          -->     Liste mit Stringwerten ("value1","value2","valuew" ...)
wp            -->     "w" überschreibt eine vorhandene Datei  "a" fügt einen Datensatz hinzu

Die Hauptmethode ist flexport. Mit ihr lässt sich mit jedem Aufruf eine übergebene Liste in eine Datei exportieren.
Sie erwartet data als Liste mit Strings sowie wp mit Angabe des Schreibmodus beim Aufruf der Methode.

Das Modul flexport_modul.py muss sich im Projektordner der Programmdatei für den Import befinden oder entsprechend mit Pfadangabe importiert werden.

Nutzungsbeispiel:
-----------------

 import flexport_modul as flp
 pfad = r"Z:\Python Projekte Code\tests"
 fp = flp.flxp(pfad, "testdatei", "txt",";")
 fp.flexport(["1234","4545","4545"], "a")
 
 
 --------------------
 _//____m4rc0k15___//
 --------------------
