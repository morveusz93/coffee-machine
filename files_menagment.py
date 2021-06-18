import json


def load_file(filename):
    """ Loads data from json file and returns it as dictionary. 
    As parametr takes 'resources' or 'menu' - depends what file you want to open"""
    with open (f'{filename}.txt') as json_file:
        data_from_file = json.load(json_file)
    return data_from_file


def save_file(current_resources):
    """ Saves current resources to txt file """
    with open ("resources.txt", "w") as json_file:
        json.dump(current_resources, json_file)

