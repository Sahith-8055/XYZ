'''
Write a function to print a dictionary with the keys in sorted order along with the
frequency of each word. Display the frequency values using “#” as a text based graph
'''
def frequency_graph(dictionary):
    '''Freqency function'''
    sorted_dict = sorted(dictionary.keys())
    for each_word in sorted_dict:
        print(each_word, '-', '#'*dictionary[each_word])
def main():
    '''Main function'''
    dictionary = eval(input())
    frequency_graph(dictionary)
if __name__ == '__main__':
    main()
