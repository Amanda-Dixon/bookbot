## Function that counts the number of words in a text

def get_num_words(text):
    words = text.split()
    n = 0
    for word in words:
          n +=1
    return n