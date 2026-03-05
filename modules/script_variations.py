import random


def generate_variations(script):

    variations = []

    for i in range(5):

        variations.append(

            script + f"\n\nVariation style {i}"

        )

    return variations
