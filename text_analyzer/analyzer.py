"""
Text analysis functions: count words, count characters,
count vowels, find the most repeated word, and reverse text.
"""

def count_words(text):
    """Counts the number of words in a text.

    Args:
        text (str): the text to analyze.

    Returns:
        int: number of words.
    """
    words = text.split()
    return len(words)

def count_characters(text, include_spaces=True):
    """Counts the number of characters in a text.

    Args:
        text (str): the text to analyze.
        include_spaces (bool): whether to include spaces in the count. Defaults to True.

    Returns:
        int: number of characters.
    """
    if include_spaces:
        return len(text)
    else:
        return len(text.replace(" ", ""))

def count_vowels(text):
    """Counts the number of vowels in a text.

    Args:
        text (str): the text to analyze.

    Returns:
        int: number of vowels.
    """
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count

def most_common_word(text):
    """Finds the most frequently repeated word in a text.

    Args:
        text (str): the text to analyze.

    Returns:
        tuple: (word, count) of the most common word.
    """
    words = text.lower().split()
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    most_common = max(word_count, key=word_count.get)
    return most_common, word_count[most_common]

def reverse_text(text):
    """Reverses the characters in a text.

    Args:
        text (str): the text to reverse.

    Returns:
        str: the reversed text.
    """
    return text[::-1]