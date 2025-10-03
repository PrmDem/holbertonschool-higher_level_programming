#!/usr/bin/python3

"""Serialises a python dictionary into xml."""

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """serialises a python dictionary
    and saves it in an xml file.

    Args:
        dictionary (dict): python dictionary to serialise
        filename (str): name of the xml file to create
    """
    xml_data = ET.Element('data')

    for key, value in dictionary.items():
        subElem = ET.SubElement(xml_data, key)
        subElem.text = value

    b_xml = ET.tostring(xml_data)
    with open(filename, "wb") as f:
        f.write(b_xml)


def deserialize_from_xml(filename):
    """reads the xml file to deserialise a Python dictionary

    Args:
        filename (str): name of the xml file to read

    Return:
        a deserialised Python dictionary
    """
    xml_tree = ET.parse(filename)
    root = xml_tree.getroot()

    py_dict = {}

    for child in root:
        py_dict[child.tag] = child.text

    return py_dict
