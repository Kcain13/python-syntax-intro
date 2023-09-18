def print_upper_words(words):
    # uppercase the word, one word per line

    for word in words:
        print(word.upper())

def filter_print_upper_words(words):
    # filter words starting with specific letter, case insensitive

    for word in words:
        if word.startswith("e") or word.startswith("E"):
            print(word.upper())

def multi_filter_print_words(words):
    # filter by multiple criteria 
    for word in words:
        for letter in must_start_with:
            if word.startswith(letter):
                print(word.upper())
                break