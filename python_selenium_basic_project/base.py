from xml.etree import ElementTree


class BaseClass:

    def __init__(self, driver):
        self.driver = driver

    @staticmethod
    def import_config(attribute):
        xml = ElementTree.parse("./configuration/config.xml")
        return xml.find(attribute).text

