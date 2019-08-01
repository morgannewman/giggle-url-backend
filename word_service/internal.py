import os
import json

# Loads all dictionaries into memory
dicts = {}
for file_name in os.listdir("word_service/dicts"):
    name = file_name.rstrip(".json")

    with open("word_service/dicts/{}".format(file_name), "r") as f:
        dicts[name] = json.load(f)


class PARTS:
    """
    Enum of word parts
    """

    noun_plural = "noun_plural"
    noun_singular = "noun_singular"
    adjective = "adjective"
    adverb = "adverb"
    superlative = "superlative"
    verb_past = "verb_past"
    verb_present = "verb_present"
    verb_progressive = "verb_progressive"
    animal = "animal"


combinations = {
    "adj_sup_ns": [PARTS.adjective, PARTS.superlative, PARTS.noun_singular],
    "adv_vprog_np": [PARTS.adverb, PARTS.verb_progressive, PARTS.noun_plural],
    "adv_vprog_an": [PARTS.adverb, PARTS.verb_progressive, PARTS.animal],
    "adv_vpast_ns": [PARTS.adverb, PARTS.verb_past, PARTS.noun_singular],
    "adv_vpast_an": [PARTS.adverb, PARTS.verb_past, PARTS.animal],
}
