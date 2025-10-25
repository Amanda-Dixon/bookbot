from stats import get_num_words, get_num_chars

## to import the text from a filepath
def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()


def main():

## to count number of words
    filepath = "./books/frankenstein.txt"
    text = get_book_text(filepath)
    num_words = get_num_words(text)
    print (f"Found {num_words} total words")

## to count number of times characters appear
    num_characters = get_num_chars(text)
    print(num_characters)

main()
