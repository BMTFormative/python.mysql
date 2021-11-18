#from xml.etree.ElementTree import ElementTree as ET
import xml.etree.ElementTree as ET

xml = ET.parse("cnr.xml")
cnr=xml.getroot()

for emp in cnr:
    print(emp.attrib)
    
'search in all beacon prenom'
prenom = cnr.findall("./prenom")    