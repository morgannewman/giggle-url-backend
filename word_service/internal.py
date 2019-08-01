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

combinations_list = [
    "adj_sup_ns",
    "adv_vprog_np",
    "adv_vprog_an",
    "adv_vpast_ns",
    "adv_vpast_an",
]


def get_seq(combination, part):
    return "{}_{}_seq".format(combination, part)
