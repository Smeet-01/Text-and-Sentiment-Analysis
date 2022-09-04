import pandas as pd
import numpy as np

def list_creator(txt_file):
    file1 = open(txt_file, 'r+')
    file2 = []
    file2 = file1.read()
    file1.close()
    for word in file2:
        word.replace('\n', '')
    return file2


positive_words = list_creator("positive-words.txt")
negative_words = list_creator("negative-words.txt")
auditor_stopwords = list_creator("StopWords_Auditor.txt")
currency_stopwords = list_creator("StopWords_Currencies.txt")
datetime_stopwords = list_creator("StopWords_DatesandNumbers.txt")
generic_stopwords = list_creator("StopWords_Generic.txt")
long_generic_stopwords = list_creator("StopWords_GenericLong.txt")
geographic_stopwords = list_creator("StopWords_Geographic.txt")
name_stopwords = list_creator("StopWords_Names.txt")
