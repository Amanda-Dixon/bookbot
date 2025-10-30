from stats import get_num_words, get_num_chars, sorted_chars
import sys

## to import the text from a filepath
def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()
    
def print_report(filepath, num_words, sorted_character_list):
    ## to print beginning of BOOKBOT output
    print ("============ BOOKBOT ============")
    print (f"Analyzing book found at {filepath}...")
    print ("----------- Word Count ----------")
    print (f"Found {num_words} total words")
    print ("--------- Character Count -------")

## to print only alphabetical characters
    for entry in sorted_character_list:
        character = entry["char"]
        if character.isalpha() == True:
            print (f"{entry["char"]}: {entry["num"]}")

## to print end of BOOKBOT output
    print ("============= END ===============")

    
def main():

## error message if two sys.argv entries aren't included
    if len(sys.argv) != 2:
        print ("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

## to count number of words
#    filepath = "./books/frankenstein.txt"
    filepath = sys.argv[1]
    text = get_book_text(filepath)
    num_words = get_num_words(text)
## to count number of times characters appear
    num_characters = get_num_chars(text)
## to create an ordered list of dictionaries of characters and their values
    sorted_character_list = sorted_chars(num_characters)
## to print the report   
    print_report(filepath, num_words, sorted_character_list)

main()
