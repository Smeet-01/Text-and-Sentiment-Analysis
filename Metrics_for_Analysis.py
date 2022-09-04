import List_of_words as lw
from nltk.tokenize import wordpunct_tokenize
from nltk.tokenize import sent_tokenize
from nltk.tokenize import SyllableTokenizer
import re
import pandas as pd

pos_score_ls =[]
neg_score_ls =[]
polar_score_ls =[]
sub_score_ls =[]
avg_sent_len_ls =[]
per_complex_words_ls =[]
fog_index_ls =[]
avg_word_per_sent_ls =[]
comp_word_count_ls =[]
avg_syll_ls =[]
pronoun_ls =[]
avg_word_len_ls =[]
word_count_ls =[]



def Metrics(file):
    # We open the txt file.
    textfile1 = open(file, 'r',encoding='mbcs',errors='ignore')
    textfile2 = []
    textfile2 = textfile1.read()
    textfile1.close()
    
    # We make a list of the positive and negative words 
    positive_words = lw.positive_words.split()
    negative_words = lw.negative_words.split()
    
    # We tokenize words from the text we obtained from the txt file and eliminate punctuation signs and symbols
    words = wordpunct_tokenize(textfile2)
    words1 = [word for word in words if word.isalpha()]
    
    # We tokenize the sentences similarly
    sentences = sent_tokenize(textfile2, language='english')
    
    # We eliminate stop words 
    lst = []
    for word in words1:
        if word in lw.auditor_stopwords.split():
            pass
        elif word in lw.currency_stopwords.split():
            pass
        elif word in lw.datetime_stopwords.split():
            pass
        elif word in lw.generic_stopwords.split():
            pass 
        elif word in lw.geographic_stopwords.split():
            pass
        elif word in lw.long_generic_stopwords.split():
            pass
        elif word in  lw.name_stopwords.split():
            pass
        else:
            lst.append(word)
            
    # Function to calculate positivity score   
    positivity_score = 0
    positivity_score_list = []
    for i in lst:
        if i in positive_words:
            positivity_score += 1
            positivity_score_list.append(i)
        else:
            pass

    # Function to calculate negativity score
    negativity_score = 0 
    negativity_score_list = []
    for i in lst:
        if i in negative_words:
            negativity_score += 1
            negativity_score_list.append(i)
        else:
            pass
        
    # Polarity score 
    polarity_score = round((positivity_score - negativity_score)/((positivity_score + negativity_score) + 0.000001),4)
    
    # Subjectivity score
    subjectivity_score = round((positivity_score + negativity_score)/(len(lst) + 0.000001), 4)
    
    # Average sentence length
    avg_sentence_length = round(len(words1)/len(sentences),4)
    
    # Percentage of complex words i.e., words with more than two syllables
    SSP = SyllableTokenizer()
    complex_words = []
    for token in words1:
        SSP.tokenize(token)
        if (len(SSP.tokenize(token))) > 2:
            complex_words.append(token)

    percentage_of_complex_words = round((len(complex_words)/len(words1)) * 100, 4)
    
    # Gunning fog index
    fog_index = round(0.4 * (avg_sentence_length + percentage_of_complex_words),4)
    
    # Average number of words in a sentence
    avg_word_per_sent = round(len(words1)/len(sentences),4)
    
    # Count of complex words
    complex_word_count = len(complex_words)
    
    # Count of all words
    word_count = len(words1)
    
    # Syllable count for every word in the text. The commented code creates a dictionary where the key:value pair represents the word and its syllable count respectively.
    syllable_count_per_word = [(len(SSP.tokenize(token)))for token in words1]
    # res = {}
    # for word in words1:
    #     for value in syllable_count_per_word:
    #         res[word] = value
    #         syllable_count_per_word.remove(value)
    #         break  

    # Average number of syllables per word
    average_syllable_per_word = sum(syllable_count_per_word)/len(syllable_count_per_word)
    
    # Pronouns used in the text
    words1_str = ' '.join(map(str, words1))
    pronounRegex = re.compile(r'\b(I|we|me|my|ours|(?-i:us))\b',re.I)
    pronouns = pronounRegex.findall(words1_str)
    
    # Average word length
    average_word_length = sum([len(i) for i in words1])/len([len(i) for i in words1])
    
    
    word_count_ls.append(word_count)
        
    print(f"The positivity score is: {positivity_score}")
    pos_score_ls.append(positivity_score)
    
    print(f"The negativity score is: {negativity_score}")
    neg_score_ls.append(negativity_score)
    
    print(f"The polarity score is: {polarity_score}")
    polar_score_ls.append(polarity_score)
    
    print(f"The subjectivity score is: {subjectivity_score}")
    sub_score_ls.append(subjectivity_score)
    
    print(f"The average sentence length is: {avg_sentence_length}")
    avg_sent_len_ls.append(avg_sentence_length)
    
    print(f"The percentage of complex words is: {percentage_of_complex_words} %")
    per_complex_words_ls.append(percentage_of_complex_words)
    
    print(f"The Gunning fog index score is: {fog_index}")
    fog_index_ls.append(fog_index)
    
    print(f"The average number of words in a sentence is: {avg_word_per_sent}")
    avg_word_per_sent_ls.append(avg_word_per_sent)
    
    print(f"The count of complex words is: {complex_word_count}")
    comp_word_count_ls.append(complex_word_count)

    print(f"The average syllable count per word is: {average_syllable_per_word}")
    avg_syll_ls.append(average_syllable_per_word)
    
    print(f"The pronouns used in the text are: {pronouns}")
    pronoun_ls.append(pronouns)

    print(f"The average length of words expressed in characters is: {average_word_length}")
    avg_word_len_ls.append(average_word_length)
  

output_files = []
for i in range(1,151):
    output_files.append(f'Outputs/{i}.txt')


c = 1

for i in output_files:
    Metrics(i)
    print('\n')
    c +=1
    print(c)


df = pd.read_excel('Output_Data_Structure-Copy.xlsx')


df.insert(14, "AVG WORD LENGTH", avg_word_len_ls)

file_name = 'Output_Data_Structure-1.xlsx'
  
# saving the excel
df.to_excel(file_name)

