# SETUP. You don't need to worry for now about what this code does or how it works. If you're ever curious about the 
# code behind these exercises, it's available under an open source license here: https://github.com/Kaggle/learntools/
from learntools.core import binder; binder.bind(globals())
from learntools.python.ex6 import *
print('Setup complete.')

a = ""
length = 0
q0.a.check()

b = "it's ok"
length = 7
q0.b.check()

c = 'it\'s ok'
length = 7
q0.c.check()

d = """hey"""
length = 3
q0.d.check()

e = '\n'
length = 1
q0.e.check()

def is_valid_zip(zip_code):
    """Returns whether the input string is a valid (5 digit) zip code
    """
    return len(zip_code)==5 and zip_code.isdigit()

q1.check()

def word_search(doc_list, keyword):
    """
    Takes a list of documents (each document is a string) and a keyword. 
    Returns list of the index values into the original list for all documents 
    containing the keyword.

    Example:
    doc_list = ["The Learn Python Challenge Casino.", "They bought a car", "Casinoville"]
    >>> word_search(doc_list, 'casino')
    >>> [0]
    """
    contain_index=[]
    for doc in doc_list:
        word_list=doc.lower().split()
        for index,word in enumerate(word_list):
            word=word.rstrip(',')
            word=word.rstrip('.')
            word_list[index]=word
        if keyword.lower() in word_list:
            contain_index.append(doc_list.index(doc))
    return contain_index

q2.check()

def multi_word_search(doc_list, keywords):
    """
    Takes list of documents (each document is a string) and a list of keywords.  
    Returns a dictionary where each key is a keyword, and the value is a list of indices
    (from doc_list) of the documents containing that keyword

    >>> doc_list = ["The Learn Python Challenge Casino.", "They bought a car and a casino", "Casinoville"]
    >>> keywords = ['casino', 'they']
    >>> multi_word_search(doc_list, keywords)
    {'casino': [0, 1], 'they': [1]}
    """
    contain_index={}
    for keyword in keywords:
        contain_index[keyword]=[]
        for doc in doc_list:
            word_list=doc.lower().split()
            for index,word in enumerate(word_list):
                word_list[index]=word.rstrip(',')
                word_list[index]=word.rstrip('.')
            if keyword.lower() in word_list:
                contain_index[keyword].append(doc_list.index(doc))
    return contain_index

q3.check()
