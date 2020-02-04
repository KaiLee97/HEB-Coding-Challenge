import operator
import io
import string
import collections

def freq(input_file, output_file): 
    
    # Open input file then read contents into a string (All lower case)
    file = open(input_file)
    f = file.read().lower()
    # Dictionary to keep track of each word and its occurence
    unique_words = {}
    # Remove all punctuation then split into list of words using whitespaces
    word_list = f.translate(str.maketrans('', '', string.punctuation)).split()
    # Increment value for word if already seen, if not make a new key value pair
    for word in word_list : 
        if word in unique_words :
            unique_words[word] += 1
        else :
            unique_words[word] = 1
    file.close()
    
    newfile = open(output_file, 'w')
    # Create new sorted dictionary by using the collections library
    sorted_dict = collections.OrderedDict(sorted(unique_words.items(), key = operator.itemgetter(1), reverse=True))
    # Write into output in the correct format
    for word,freq in sorted_dict.items():
        newfile.write(word + ' | ' + (''.join(['=' for i in range(freq)]) + ' (' + str(freq)) + ')\n')
    newfile.close()
    
    
freq('input.txt', 'output.txt')