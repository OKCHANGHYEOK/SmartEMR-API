import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element

def convert_from_xml(strXML : str):
    root = ET.fromstring(strXML)

    def parse_element(element : Element):
        children = list(element)

        if not children:
            return element.text

        result = {}

        for child in children:
            value = parse_element(child)

            if child.tag in result:
                if not isinstance(result[child.tag], list):
                    result[child.tag] = [result[child.tag]]

                result[child.tag].append(value)   

            else:
                result[child.tag] = value

        return result

    return {root.tag : parse_element(root)}            