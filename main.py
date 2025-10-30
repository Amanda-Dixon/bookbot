from stats import get_num_words, get_num_chars, sorted_chars

## to import the text from a filepath
def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()
    

def main():

## to count number of words
    filepath = "./books/frankenstein.txt"
    text = get_book_text(filepath)
    num_words = get_num_words(text)


## to count number of times characters appear
    num_characters = get_num_chars(text)
#    print(num_characters)

## to create an ordered list of dictionaries of characters and their values
    sorted_character_list = sorted_chars(num_characters)

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

main()
