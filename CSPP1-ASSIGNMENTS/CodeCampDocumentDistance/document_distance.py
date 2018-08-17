'''
    Document Distance - A detailed description is given in the PDF
'''
import math
stopwords = "stopwords.txt"
def similarity(dict1, dict2):
    '''
        Compute the document distance as given in the PDF
    '''
    list1 = dict1.split(' ')
    list2 = dict2.split(' ')
    list3 = list1 + list2
    dict3 = {}
    for word in list3:
        if word not in (load_stopwords(stopwords).keys()):
            for i in range(len(word)):
                if word[i] not in '1234567890!@#$%^&*()_-+?':
                    dict3[word] = (dict1.count(word), dict2.count(word))
    numerator, sum1, sum2 = 0, 0, 0
    for k in dict3:
        numerator += (dict3[k][0]*dict3[k][1])
        sum1 += dict3[k][0]**2
        sum2 += dict3[k][1]**2
        denominator = math.sqrt(sum1) * math.sqrt(sum2)
    similarity1 = (numerator / denominator)
    return similarity1
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
