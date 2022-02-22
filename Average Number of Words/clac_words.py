# Title: Average Number of Words Program
# Program created by William Schaeffer
# CPS 313
# P. 463, Exercise 6, clac words Program
# 02.08.22

# This program will calculate the average number of words per sentence / line from tex

# imports for functions

# Main Function

def main():
    
    sentence_file = open('text.txt')                # open text.txt

    total_word_count = 0                            # initialize total word count and line (sentence) count
    line = 0
    fileInput = sentence_file.readline()            # read line and store in file Input

    while fileInput != '':                          # while fileInput is not an empty string
        sentence_list = fileInput.split()           # split the sentence into a list
        word_count = len(sentence_list)             # count the elements of the list for word count
        #print('word count: ', word_count)          #for testing purposes

        total_word_count += word_count              # add word count to total word count
        
        fileInput = sentence_file.readline()        # read the next line
        
        #print('total count: ', total_word_count)   #for testing purposes
        
        line += 1                                   # increment line count
        
        #print('total line: ', line)                #for testing purposes

    average_words_per_sentence = total_word_count / line

    print('Average words per line: ', format(average_words_per_sentence, ".1f"))

    sentence_file.close

main()                                              # call main function

