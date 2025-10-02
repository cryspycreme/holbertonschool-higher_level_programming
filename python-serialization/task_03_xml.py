#!/user/bin/python3

"""
XML Module
"""

import xml.etree.ElementTree as ET
# from xml.dom import minidom

#convert dictionary to XML, save in filename
def serialize_to_xml(dictionary, filename):
    # create root element
    root = ET.Element("data")

    for key, value in dictionary.items():
        child = ET.SubElement(root, key) #create sub-element
        child.text = str(value) #assign text value
    
    #create ElementTree object
    tree = ET.ElementTree(root)
    
    # write ElementTree to filename
    tree.write(filename, encoding="utf-8")

    #convert XML to string
    xml_string = ET.tostring(root, encoding="utf-8", xml_declaration=True)

    # pretty_xml = minidom.parseString(xml_string).toprettyxml(indent="    ")

def deserialize_from_xml(filename):
    #parse the XML file
    tree = ET.parse(filename)
    root = tree.getroot()

    #return constructed dictionary
    person_dict = {child.tag: child.text for child in root}
    return person_dict