'''
    Document Distance - A detailed description is given in the PDF
'''
import math
import re
stopwords = "stopwords.txt"
def cleanup_words(input1):
    reg = re.compile('[^a-z]')
    input1 = input1.lower()
    input1 = [reg.sub('',w.strip()) for w in input1.split(' ')]
    return input1
def remove_stopwords(input1,input2):
    d={}
    d=load_stopwords(stopwords)
    word_list1 = cleanup_words(input1)
    word_list2 = cleanup_words(input2)
    word_list  = word_list1 + word_list2
    dictionary = {}
    for  word in word_list:
        if word not in d and len(word) > 0:
            dictionary[word] = (word_list1.count(word),word_list2.count(word))
    return dictionary        
def similarity(dict1, dict2):
    '''
        Compute the document distance as given in the PDF
    '''
    dictionary = {}
    dictionary = remove_stopwords(dict1,dict2)
    numerator, denominator1, denominator2 = 0, 0, 0
    for d in dictionary.values():    
        numerator += d[0] * d[1]
        denominator1 += (d[0]**2)
        denominator2 += (d[1]**2)
        denominator = math.sqrt(denominator1) * math.sqrt(denominator2)
    return (numerator / denominator)
def load_stopwords(filename):
    '''
        loads stop words from a file and returns a dictionary
    '''
    stopwords = {}
    with open(filename, 'r') as filename:
        for line in filename:
            stopwords[line.strip()] = 0
    return stopwords
def main():
    '''
        take two inputs and call the similarity function
    '''
    input1 = input().lower()
    input2 = input().lower()
    print(similarity(input1, input2))
if __name__ == '__main__':
    main()
