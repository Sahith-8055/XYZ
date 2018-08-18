'''
    Tiny Search Engine - Part 1 - Build a search index
    In this programming assingment you are given with some text documents as input.
    Complete the program below to build a search index. Don't worry, it is explained below.
    A search index is a python dictionary.
    The keys of this dictionary are words contained in ALL the input text documents.
    The values are a list of documents such that the key/word appears in each document atleast once.
    The document in the list is represented as a tuple.
    The tuple has 2 items. The first item is the document ID.
    Document ID is represented by the list index.
    For example: the document ID of the third document in the list is 2
    The second item of the tuple is the frequency of the word occuring in the document.
    Here is the sample format of the dictionary.
    {
        word1: [(doc_id, frequency),(doc_id, frequency),...],
        word2: [(doc_id, frequency),(doc_id, frequency),...],
        .
        .
    }
'''
import re
FILENAME = "stopwords.txt"
# helper function to load the stop words from a file
def load_stopwords(filename):
    '''
        loads stop words from a file and returns a dictionary
    '''
    stopwords = {}
    with open(filename, 'r') as f_stopwords:
        for line in f_stopwords:
            stopwords[line.strip()] = 0
    return stopwords
def word_list(text):
    '''
        Change case to lower and split the words using a SPACE
        Clean up the text by removing all the non alphabet characters
        return a list of words
    '''
    reg = re.compile('[^a-z]')
    str1 = ''.join(text)
    str1 = [reg.sub('', k.strip()) for k in str1.split(' ')]
    return str1
def remove_stopwords(text):
    '''Remove the unwanted words'''
    d_input = {}
    d_input = load_stopwords(FILENAME)
    word_list1 = word_list(text)
    dictionary = {}
    for  word in word_list1:
        if word not in d_input and len(word) > 0:
            dictionary[word] = word_list1.count(word)
    return dictionary
def build_search_index(docs):
    '''
        Process the docs step by step as given below
    '''
    # initialize a search index (an empty dictionary)
    # iterate through all the docs
    # keep track of doc_id which is the list index corresponding the document
    # hint: use enumerate to obtain the list index in the for loop
        # clean up doc and tokenize to words list
        # add or update the words of the doc to the search index
    # return search index
    search_index = {}
    docs = remove_stopwords(docs)
    for index, word in enumerate(docs):
        if word in search_index.keys():
            search_index[word].append(index)
        else:
            search_index[word] = [index]
    return search_index
# helper function to print the search index
# use this to verify how the search index looks
def make_indices(list1):
    ''' Function to find indices '''
    total = {}
    for name in list1.keys():
        total[name] = build_search_index(list1[name])
    return total
def full_indices(dict1):
    '''Function to find full indices '''
    total_indices = {}
    for name in dict1.keys():
        for word in dict1[name].keys():
            if word in total_indices.keys():
                if name in total_indices[word].keys():
                    total_indices[word][name].extend(dict1[name][word][:])
                else:
                    total_indices[word][name] = dict1[name][word]
    return total_indices
def print_search_index(index):
    '''
        print the search index
    '''
    keys = sorted(index.keys())
    for key in keys:
        print(key, " - ", index[key])
# main function that loads the docs from files
def main():
    '''
        main function
    '''
    # empty document list
    documents = []
    # iterate for n times
    lines = int(input())
    # iterate through N times and add documents to the list
    for i in range(lines):
        documents.append(input())
        i += 1
    # call print to display the search index
    print_search_index(build_search_index(documents))
if __name__ == '__main__':
    main()
