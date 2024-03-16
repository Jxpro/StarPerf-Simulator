import xml.etree.ElementTree as ET


def xml_to_dict(element):
    if len(element) == 0:
        return element.text
    result = {}
    for child in element:
        child_data = xml_to_dict(child)
        if child.tag in result:
            if type(result[child.tag]) is list:
                result[child.tag].append(child_data)
            else:
                result[child.tag] = [result[child.tag], child_data]
        else:
            result[child.tag] = child_data
    return result


def read_xml_file(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()
    return {root.tag: xml_to_dict(root)}
