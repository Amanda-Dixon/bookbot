from stats import get_num_words

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()


def main():

    filepath = "./books/frankenstein.txt"
    text = get_book_text(filepath)
    num_words = get_num_words(text)
    print (f"Found {num_words} total words")


main()
