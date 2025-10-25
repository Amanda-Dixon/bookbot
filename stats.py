## Function that counts the number of words in a text

def get_num_words(text):
    words = text.split()
    n = 0
    for word in words:
          n +=1
    return n

## Function that counts the number of times a character appears in a text
## (Including special characters and spaces)

def get_num_chars(text):
     num_chars = {}
     lower_case = text.lower()           
     for char in lower_case:
            if char in num_chars:
                  num_chars[char] += 1                
            else:
                  num_chars[char] = 1      
     return num_chars



