"""Module to handle the mock data fed to the database"""
import random


def _load_wordlist(filename):
    """Loads a wordlist and returns a list of lines from the file"""
    filedirs = __file__.split("/")[:-1] + ["..", "wordlists"]
    filepath = "/".join(filedirs + [filename])
    with open(filepath, "r") as file:
        words = file.read().strip().split("\n")
    return words


def load_users(db_size):
    """Loads a list of tuples containing users"""
    if db_size > 999 or db_size < 1:
        raise Exception("db_size must be between 0 and 1000")

    first_names = _load_wordlist("first_names.txt")
    first_names = [n.title() for n in first_names]
    random.shuffle(first_names)
    first_names = first_names[:db_size]

    last_names = _load_wordlist("last_names.txt")
    last_names = [n.title() for n in last_names]
    random.shuffle(last_names)
    last_names = last_names[:db_size]

    passwords = _load_wordlist("passwords.txt")
    random.shuffle(passwords)
    passwords = passwords[:db_size]

    data_group = (first_names, last_names, passwords)

    users = []
    for i, group in enumerate(zip(*data_group)):
        user = (i+1, repr(group[0]), repr(group[1]), repr(group[2]))
        users.append("(%d, %s, %s, %s)" % user)

    return users
