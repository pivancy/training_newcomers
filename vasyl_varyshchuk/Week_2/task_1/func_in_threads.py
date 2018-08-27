""""
This module returns random size of file name from list by processing elements in separate threads
"""

import random
import string
from threading import Thread


number_of_threads = 3
length_of_list = number_of_threads * 100


def recognize_file_type(file_name):
    """This function returns extension of file passing file name as parameter"""
    _, extension = file_name.split('.')
    return extension


def generate_file_names_list():
    """
    This function generate list of files with random names.
    Length of list is specified by global variable
    len_of_list which value depend on number of thread.
    """
    extensions = ['txt', 'zip', 'ini', 'jpg', 'ttf']
    file_names = []
    for i in range(length_of_list):
        file_name = ''.join([random.choice(string.ascii_lowercase) for j in range(5)])
        full_file_name = '.'.join([file_name, random.choice(extensions)])
        file_names.append(full_file_name)
    return file_names


def txt_handler():
    return random.randint(100, 450)


def zip_handler():
    return random.randint(500, 700)


def jpg_handler():
    return random.randint(800, 1000)


def ttf_handler():
    return random.randint(1100, 1300)


def ini_handler():
        return random.randint(1300, 1500)


handlers = {
    'txt': txt_handler,
    'zip': zip_handler,
    'jpg': jpg_handler,
    'ttf': ttf_handler,
    'ini': ini_handler
 }


def choose_handlers(file_names_list):
    """This function runs handlers for corresponding file extensions"""
    extensions = map(recognize_file_type, file_names_list)
    for extension in extensions:
        handler = handlers[extension]
        result = handler()
        print('Generated size for .{} is: {}'.format(extension, result))


def run_executors(list_of_file_names):
    """Function which returns random size for file names from a list."""
    for i in range(number_of_threads):
        thread = Thread(target=choose_handlers, args=(list_of_file_names,))
        thread.start()
        thread.join()
        print('------------------------Processing is complete for {}-------------------------'.format(thread.name))


# Example of use
list_of_files = generate_file_names_list()
run_executors(list_of_files)
