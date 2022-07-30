import configparser


def get_locator():
    config = configparser.ConfigParser()
    config.read('E:\\Python\\Projects\\Ryanair\\locators\\locators.ini')

    return config

