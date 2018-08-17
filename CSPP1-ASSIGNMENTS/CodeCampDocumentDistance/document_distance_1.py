'''
    Document Distance - A detailed description is given in the PDF
'''
import math
FILENAME = "stopwords.txt"
def similarity(dict1, dict2):
    '''
        Compute the document distance as given in the PDF
    '''
    list1 = ''
    for i in dict1:
        for j in i:
            if j not in '!@#$%^&*()_+-=,.?1234567890':
                if j not in "'":
                    list1 += j
    list2 = ''
    for i in dict2:
        for j in i:
            if j not in '!@#$%^&*()_+-=,.?1234567890':
                if j not in "'":
                    list2 += j
    list1 = dict1.split()
    list2 = dict2.split()
    list3 = list1 + list2
    dict3 = {}
    for word in list3:
        if word not in load_stopwords(FILENAME).keys():
            dict3[word] = (dict1.count(word), dict2.count(word))
    numerator, add1, add2 = 0, 0, 0
    for k in dict3:
        numerator += (dict3[k][0]*dict3[k][1])
        add1 += dict3[k][0]**2
        add2 += dict3[k][1]**2
    denominator = math.sqrt(add1) * math.sqrt(add2)
    return numerator / denominator
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
