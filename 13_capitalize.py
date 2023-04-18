def capitalize(phrase):
    """Capitalize first letter of first word of phrase.

        >>> capitalize('python')
        'Python'

        >>> capitalize('only first word')
        'Only first word'
    """

    swapped = phrase[0].upper()

    phrase_no_first_letter = phrase[1::]

    swapped += phrase_no_first_letter

    return swapped
