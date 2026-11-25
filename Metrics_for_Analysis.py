from nltk.tokenize import wordpunct_tokenize
from nltk.tokenize import sent_tokenize
from nltk.tokenize import SyllableTokenizer



class Metrics:

    #Pass text to be analyzed to the Instance. Text is broken up in two lists, words and sentences for analysis.
    def __init__(self, Text):
        words = wordpunct_tokenize(Text)
        self.textwords = [word.lower() for word in words if word.isalpha()]
        sentences = sent_tokenize(Text, 'english')
        self.sentences = [sent for sent in sentences]
        self.avg_sentence_length = round(len(self.textwords) / len(self.sentences), 4) if self.sentences else 0.0
        
    #Positivity Score
    def positivity_score(self, positivityList):
        positivity_set = set(positivityList)
        return sum(1 for word in self.textwords if word in positivity_set)
    
    #Negativity Score
    def negativity_score(self, negativityList):
        negativity_set = set(negativityList)
        return sum(1 for word in self.textwords if word in negativity_set)
    
    #Polarity Score  - ranges between -1 to 1
    def polarity_score(self, positivity_score: int = 0, negativity_score: int = 0):
        return round((positivity_score - negativity_score)/((positivity_score + negativity_score) + 0.000001),4)
    
    #Subjectivity Score - ranges from 0 to 1
    def subjectivity_score(self, positivity_score: int = 0, negativity_score: int = 0):
        return round((positivity_score + negativity_score)/(len(self.textwords) + 0.000001), 4)
    
    #Complexity of text - percentage of words in the text that have three or more syllables
    def text_complexity(self):
        if not self.textwords:
            return 0.0
        SSP = SyllableTokenizer()
        complex_words = [token for token in self.textwords if len(SSP.tokenize(token)) > 2]
        comp_words_pcent = round((len(complex_words)/len(self.textwords)) * 100, 4)
        return comp_words_pcent


    """
    Gunning Fog Index - In linguistics, the Gunning fog index is a readability test for English writing. 
    The index estimates the years of formal education a person needs to understand the text on the first reading. 
    For instance, a fog index of 12 requires the reading level of a United States high school senior (around 18 years old). 
    The test was developed in 1952 by Robert Gunning, an American businessman who had been involved in newspaper and textbook publishing
    
    https://en.wikipedia.org/wiki/Gunning_fog_index
    """
    
    def GFI(self, text_complexity):
        return round(0.4 * (self.avg_sentence_length + text_complexity), 4)
    

    #Calculates the average number of syllables for words in the given text
    def Average_syllable_count(self):
        if not self.textwords:
            return 0.0
        SSP = SyllableTokenizer()
        syllable_count_per_word = [len(SSP.tokenize(token)) for token in self.textwords]
        return round((sum(syllable_count_per_word)/len(syllable_count_per_word)), 4)
             

    

    

    
    

        





