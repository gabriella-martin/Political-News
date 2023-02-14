
from data_pipeline import list_of_headlines, links
import nltk
import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
import pandas as pd

from nltk.tokenize import word_tokenize


list_of_headlines = list_of_headlines()

class ProcessHeadlines:

    def __init__(self, list_of_headlines):
        self.list_of_headlines = list_of_headlines

    def remove_punctuation(self):
        list_of_headlines_no_punc = []
        for headline in self.list_of_headlines:
            headline = headline.translate(str.maketrans('', '', string.punctuation))
            list_of_headlines_no_punc.append(headline)
        return(list_of_headlines_no_punc)

    def remove_stop_words(self):
        list_of_headlines = self.remove_punctuation()
        list_of_headlines_no_stop = []
        for headline in list_of_headlines:
            headline_tokens = word_tokenize(headline)
            headline = [word for word in headline_tokens if not word in stopwords.words('english')]
            list_of_headlines_no_stop.append(headline)
        return(list_of_headlines_no_stop)

    def lemmatise_words(self):
        list_of_headlines = self.remove_stop_words()
        lemma = nltk.wordnet.WordNetLemmatizer()
        for headline in list_of_headlines:
            for index, word in enumerate(headline):
                headline[index] = (lemma.lemmatize(word))
        return(list_of_headlines)
    
    def turn_list_of_words_to_sentence(self):
        list_of_headlines = self.lemmatise_words()
        formatted_list_of_headlines = []
        for headline_words in list_of_headlines:
            headline_formatted = " ".join(headline_words)
            formatted_list_of_headlines.append(headline_formatted)
        return(formatted_list_of_headlines)

lw_len = len(list_of_headlines[0])
rw_len = len(list_of_headlines[1])
mw_len = len(list_of_headlines[2])

print(rw_len)
print(lw_len)
print(mw_len)

lists = links()
list_of_headlines = list_of_headlines[0] + list_of_headlines[1] + list_of_headlines[2]
a = ProcessHeadlines(list_of_headlines)
formatted_list_of_headlines = a.turn_list_of_words_to_sentence()

count_vectorizer = CountVectorizer()
sparse_matrix = count_vectorizer.fit_transform(formatted_list_of_headlines)

doc_term_matrix  = sparse_matrix.todense()


df = pd.DataFrame(doc_term_matrix, 
                  columns=count_vectorizer.get_feature_names_out()
                  )

from sklearn.metrics.pairwise import cosine_similarity
matrix = (cosine_similarity(df, df))

matches = {}

for ind, row in enumerate(matrix):
    matches[ind] = []
    for index, value in enumerate(row):
        if (value >= 0.28):
            if ind != index:
                matches[ind].append(index)


lists = lists[0] + lists[1] + lists[2]                    
                    
print('done')
import streamlit as st

full_matches = {}

used = []

collection = [}
collection_of_collection = []
for key, value in matches.items():
    collection = []
    if key not in used:
        if len(value) >2:
            headline = (list_of_headlines[key])
            link= (lists[key])
            used.append(key)
            collection.append(headline)
            collection.append(link)
            for i in value:
                headline = (list_of_headlines[i])
                link = (lists[i])
                used.append(i)
                collection.append(headline)
                collection.append(link)
            
            else: 
                collection_of_collection.append(collection)






for collection in collection_of_collection:
    section_choice = []
    dm = 0
    g = 0
    i = 0
    for a in range(1,len(collection),2):
        link = (collection[a])
        if len(section_choice) < 8:
            if 'dailymail' in link and dm <1:
                section_choice.append('Right Wing')
                section_choice.append(collection[a-1])
                section_choice.append(link)
                dm +=1

            elif 'guardian' in link and g<1:
                section_choice.append('Left Wing')
                section_choice.append(collection[a-1])
                section_choice.append(link)
                g+=1
            elif 'independent' in link and i<1:
                section_choice.append('Center') 
                section_choice.append(collection[a-1])
                section_choice.append(link)
                i+=1
    if len(section_choice)>3:
        st.write('**Related Topic**')
        for i in range(0,len(section_choice)):
            st.write(section_choice[i], unsafe_allow_html=True)
        st.write('----------------')
    
        


