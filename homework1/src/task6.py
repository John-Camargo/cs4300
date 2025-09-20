# impirted for better word parsing using re.findall()
import re

# function that counts the numbers of words in a file, regardless of punctuation and newlines
def word_count(filename=""):
    # if no filename arg passed to function, use task6_read_me.txt as default, else use provided file/path
    if filename == "":
        filename = "src/task6_read_me.txt"
    # open the given file for reading
    with open(filename, 'r') as file:
        # extract all file contents into plaintext var
        plaintext = file.read()
        # split the file contents into list of separate words using re.findall() and regex pattern
        # - \w+: sequences of word characters
        # - \b: sets boundary for beginning/end of word
        words = re.findall(r'\b\w+\b', plaintext)
        # return num elements in words, aka num words
        return len(words)
    

print(word_count())
print(word_count("src/task6_random_text.txt"))