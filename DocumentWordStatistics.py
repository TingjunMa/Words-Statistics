from tkinter import filedialog
from time import *

def open_txt_file():
    root = filedialog.Tk()
    filename =  filedialog.askopenfilename(initialdir = "F:/",title = "Choose your file",filetypes = (("txt files","*.txt"),("all files","*.*")))
    #print (filename)
    root.withdraw()
    file = open(filename,'r').read()
    return file 

"""
def normalize(s):
    
    symbol = {'.',',',';',':','?','!','(',')'}
    result = ' '
    for letters in s.lower():
        if letters in keep:
            result = result+letters
        elif letters in symbol:
            result = result+' '
    return result
"""

def build_dict(s):
    #s = normalize(s)                               Using this function will result in huge running time in large txt file
    words = s.split()
    dict = {}
    for each_word in words:
        each_word=each_word.lower()
        keep = {'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','-',"'"}
        filter_result = ''
        for letters in each_word:
            if letters in keep:
                filter_result = filter_result+letters
        each_word = filter_result    
        if  each_word in dict:
            dict[each_word] += 1
        else:
            dict[each_word] = 1
    return dict

def statistics(txt_file):
    num_chars = len(txt_file)
    num_lines = txt_file.count('\n') +1
    print("Calculating...\n")
    dictionary = build_dict(txt_file)   
    num_words = sum(dictionary[each_word] for each_word in dictionary)
    list = [(dictionary[each_word],each_word) for each_word in dictionary]
    list.sort()
    list.reverse()
    print("The file has:")
    print("    %s characters" % num_chars)
    print("    %s lines" % num_lines)
    print("    %s words" % num_words)
    print("\nThe top 50 most frequent words are:")
    i = 1
    for count,word in list[:50]:
        print("%2s. %6s %s" % (i,count,word))
        i += 1

start_time = time()
txt_file = open_txt_file()
statistics(txt_file)
end_time = time()
print("Elapsed Time: %.3f s" % (end_time-start_time))