import json
import os
from random import randint

from django.db import connection

from .internal import combinations_list, combinations, get_seq


# Loads all dictionaries into memory
dicts = {}
for file_name in os.listdir("word_service/dicts"):
    name = file_name.rstrip(".json")

    with open("word_service/dicts/{}".format(file_name), "r") as f:
        dicts[name] = json.load(f)


def get_random_combination():
    return combinations_list[randint(0, len(combinations_list) - 1)]


def get_next_ints_in_seq(combination, parts):
    """
    The database stores an arbitrary sequence number for each
    (combination, part). Because each combination has 3 parts,
    this function fetches all 3 at once.
    """
    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT nextval(%s), nextval(%s), nextval(%s)",
            [
                get_seq(combination, parts[0]),
                get_seq(combination, parts[1]),
                get_seq(combination, parts[2]),
            ],
        )
        ints = cursor.fetchall()
    return ints[0]


def get_next_words(parts, ints):
    """
    Using the arbitrary integer from the database for each part, we map
    this integer to a value in each dictionary (which is a list) for
    all 3 words.
    """
    words = []
    for num, part in zip(ints, parts):
        dict_words = dicts[part]
        boundary = len(dict_words) - 1
        word_index = num % boundary
        words.append(dict_words[word_index])
    return words


def get_next_giggle():
    # Select random combination
    combination = get_random_combination()
    # Get word parts in combination
    parts = combinations[combination]
    # Get next integers from combination
    ints = get_next_ints_in_seq(combination, parts)
    # Map integers to a value in dicts
    words = get_next_words(parts, ints)
    # Return string
    return words[0] + words[1] + words[2]
