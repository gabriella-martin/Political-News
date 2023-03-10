import nltk
import pandas as pd
import string
from data_pipeline import list_of_headlines, links
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

#processing data

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

lists = links()
list_of_headlines = list_of_headlines[0] + list_of_headlines[1] + list_of_headlines[2]
a = ProcessHeadlines(list_of_headlines)
formatted_list_of_headlines = a.turn_list_of_words_to_sentence()

#machine learning attempt

count_vectorizer = CountVectorizer()
sparse_matrix = count_vectorizer.fit_transform(formatted_list_of_headlines)
doc_term_matrix  = sparse_matrix.todense()
df = pd.DataFrame(doc_term_matrix, 
                  columns=count_vectorizer.get_feature_names_out()
                  )

matrix = (cosine_similarity(df, df))
matches = {}
for ind, row in enumerate(matrix):
    matches[ind] = []
    for index, value in enumerate(row):
        if (value >= 0.28):
            if ind != index:
                matches[ind].append(index)

