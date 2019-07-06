from xml.etree import ElementTree

def readFile(tag):
    file = ElementTree.parse('config.xml')
    database = file.find('database')

    return database.find(tag).text

def name():
    return readFile('name')


def user():
    return readFile('user')


def password():
    return readFile('password')


def host():
    return readFile('host')


def port():
    return readFile('port')
