import requests
from bs4 import BeautifulSoup

import streamlit as st
from streamlit_extras.image_in_tables import table_with_images

import pandas as pd

from streamlit_extras.app_logo import add_logo
add_logo("https://cdn-icons-png.flaticon.com/512/183/183412.png", height=20)

with open('styles.css') as f:
    st.markdown(f'<style>{f.read()}</style', unsafe_allow_html=True)

with st.sidebar:
    st.image('https://cdn-icons-png.flaticon.com/512/183/183412.png',width=200)
st.write("""<style>@import url('https://fonts.googleapis.com/css2?family=Mukta');html, body, [class*="css"]  {  
   font-family: 'Kanit';  
}</style>""", unsafe_allow_html=True)

# RIGHT WING PIPELINE

the_times_urls = ["https://www.thetimes.co.uk/search?filter=all&q=transgender&source=search-page", 'https://www.thetimes.co.uk/search?source=search-page&q=immigration', 'https://www.thetimes.co.uk/search?source=search-page&q=racism', 'https://www.thetimes.co.uk/search?source=search-page&q=strikes', 'https://www.thetimes.co.uk/search?source=search-page&q=brexit' ]
telegraph_urls = ['https://www.telegraph.co.uk/lgbt/', 'https://www.telegraph.co.uk/immigration/', 'https://www.telegraph.co.uk/racism/' , 'https://www.telegraph.co.uk/brexit/']

class TheTimesPipeline:
    def __init__(self, urls):
        self.urls = urls
        self.recent_ten_headlines = []
        self.recent_ten_links = []

    def get_topic_page_response(self):
        for index, url in enumerate(self.urls):
            url = url
            r = requests.get(url)
            with open(f'{index}-T', 'wb') as f:
                f.write(r.content)
    
    def open_html_and_parse(self):
        list_of_files = ['0-T','1-T', '2-T', '3-T']
        for filename in list_of_files:
            ten_headlines = []
            ten_links = []
            with open(filename, 'rb') as filename:
                soup = BeautifulSoup(filename.read(), 'html.parser')
                topic_articles = soup.find_all("li", class_="Item ArticleList-item ArticleList-item--noMedia")
                num = 0
                for i in topic_articles:
                    if num <11:
                        link = i.a['href']
                        link = 'https://www.thetimes.co.uk/' + link
                        headline = i.div.h2.text
                        ten_headlines.append(headline)
                        ten_links.append(link)
                        num +=1
            self.recent_ten_headlines.append(ten_headlines)
            self.recent_ten_links.append(ten_links)
        return self.recent_ten_headlines, self.recent_ten_links

class TelegraphPipeline:
    def __init__(self, urls):
        self.urls = urls
        self.recent_ten_headlines = []
        self.recent_ten_links = []

    def get_topic_page_response(self):
        for index, url in enumerate(self.urls):
            url = url
            r = requests.get(url)
            with open(f'{index}-Te', 'wb') as f:
                f.write(r.content)
    
    def open_html_and_parse(self):
        list_of_files = ['0-Te','1-Te', '2-Te', '3-Te']
        for filename in list_of_files:
            ten_headlines = []
            ten_links = []
            with open(filename, 'rb') as filename:
                num = 0
                soup = BeautifulSoup(filename.read(), 'html.parser')
                topic_articles = soup.find_all("article", class_="card")
                for i in topic_articles:
                    if num < 11:
                        link = i.a['href']
                        link = 'https://www.telegraph.co.uk/' + link
                        headline = i.span.text
                        ten_headlines.append(headline)
                        ten_links.append(link)
                        num +=1
                self.recent_ten_headlines.append(ten_headlines)
                self.recent_ten_links.append(ten_links)
        return self.recent_ten_headlines, self.recent_ten_links


# LEFT WING PIPELINE

guardian_urls = ['https://www.theguardian.com/society/transgender', 'https://www.theguardian.com/uk/immigration', 'https://www.theguardian.com/world/race', 'https://www.theguardian.com/politics/eu-referendum']
independent_urls = ['https://www.independent.co.uk/topic/trans','https://www.independent.co.uk/topic/uk-immigration', 'https://www.independent.co.uk/topic/racism', 'https://www.independent.co.uk/topic/brexit' ]

class GuardianPipeline:
    def __init__(self, urls):

        self.urls = urls
        self.recent_ten_headlines = []
        self.recent_ten_links = []

    def get_topic_page_response(self):

        for index, url in enumerate(self.urls):
            url = url
            r = requests.get(url)
            with open(f'{index}-G', 'wb') as f:
                f.write(r.content)
    
    def open_html_and_parse(self):
        list_of_files = ['0-G','1-G', '2-G', '3-G']
        for filename in list_of_files:
            ten_headlines = []
            ten_links = []
            with open(filename, 'rb') as filename:
                num = 0
                soup = BeautifulSoup(filename.read(), 'html.parser')
                topic_articles = soup.find_all("li", class_="fc-slice__item l-row__item l-row__item--span-1 u-faux-block-link")
                for i in topic_articles:
                    if num < 11:
                        link = i.a['href']
                        headline = (i.find('a', class_ = 'u-faux-block-link__overlay js-headline-text')).text
                        ten_headlines.append(headline)
                        ten_links.append(link)
                        num +=1

                topic_articles = soup.find_all('li', class_ = 'fc-slice__item l-list__item l-row__item l-row__item--span-1 u-faux-block-link' )
                for i in topic_articles:
                    if num < 11:
                        link = i.a['href']
                        headline = i.div.span.text
                        ten_headlines.append(headline)
                        ten_links.append(link)
                        num +=1
                self.recent_ten_headlines.append(ten_headlines)
                self.recent_ten_links.append(ten_links)

        return self.recent_ten_headlines, self.recent_ten_links

class IndependentPipeline:
    def __init__(self, urls):
        self.urls = urls
        self.recent_ten_headlines = []
        self.recent_ten_links = []

    def get_topic_page_response(self):
        for index, url in enumerate(self.urls):
            url = url
            r = requests.get(url)
            with open(f'{index}-In', 'wb') as f:
                f.write(r.content)
    
    def open_html_and_parse(self):
        list_of_files = ['0-In','1-In', '2-In', '3-In']
        for filename in list_of_files:
            ten_headlines = []
            ten_links = []
            with open(filename, 'rb') as filename:
                soup = BeautifulSoup(filename.read(), 'html.parser')
                topic_articles = soup.find_all('div', class_ ='sc-7ax485-2 emFImu article article-default')
                num = 0
                for i in topic_articles:
                    if num <11:
                        link = i.a['href']
                        link = 'https://www.independent.co.uk' + link
                        headline = i.h2.text
    
                        ten_headlines.append(headline)
                        ten_links.append(link)
                        num +=1
            self.recent_ten_headlines.append(ten_headlines)
            self.recent_ten_links.append(ten_links)
        return self.recent_ten_headlines, self.recent_ten_links

# NEUTRAL PIPELINE

i_news_links = ['https://inews.co.uk/topic/transgender', ' https://inews.co.uk/topic/immigration', 'https://inews.co.uk/topic/racism', 'https://inews.co.uk/category/news/brexit']

class INewsPipeline:
    def __init__(self, urls):
        self.urls = urls
        self.recent_ten_headlines = []
        self.recent_ten_links = []

    def get_topic_page_response(self):
        for index, url in enumerate(self.urls):
            url = url
            r = requests.get(url)
            with open(f'{index}-I', 'wb') as f:
                f.write(r.content)
    
    def open_html_and_parse(self):
        list_of_files = ['0-I','1-I', '2-I', '3-I']
        for filename in list_of_files:
            ten_headlines = []
            ten_links = []
            with open(filename, 'rb') as filename:
                num = 0
                soup = BeautifulSoup(filename.read(), 'html.parser')
          
                topic_articles = soup.find_all('div', class_ ='inews__post-hero__headline')
                for i in topic_articles:
                    if num < 11:
                        link = i.a['href']
                        headline = i.a['title']
                        ten_headlines.append(headline)
                        ten_links.append(link)
                        num +=1
                topic_articles = soup.find_all('div', 'inews__post-puff__content-headline')
                for i in topic_articles:
                    if num < 11:
                        link = i.a['href']
                        headline = i.a['title']
                        ten_headlines.append(headline)
                        ten_links.append(link)
                        num +=1
                topic_articles = soup.find_all('span','inews__post-teaser__content__headline')
                print(topic_articles)
                for i in topic_articles:
                    if num < 11:
                        link = i.a['href']
                        headline = i.a['title']
                        ten_headlines.append(headline)
                        ten_links.append(link)
                        num +=1
                topic_articles = soup.find_all('div', 'inews__post-jot__content-headline')
                for i in topic_articles:
                    if num < 11:
                        link = i.a['href']
                        headline = i.a['title']
                        ten_headlines.append(headline)
                        ten_links.append(link)
                        num +=1
            self.recent_ten_headlines.append(ten_headlines)
            self.recent_ten_links.append(ten_links)
        return self.recent_ten_headlines, self.recent_ten_links














a=INewsPipeline(urls=i_news_links)

#a.get_topic_page_response()
T_headlines_and_links = a.open_html_and_parse()
st.write(T_headlines_and_links[0][0])

'''a = TheTimesPipeline(urls=the_times_urls)
#a.get_topic_page_response()
T_headlines_and_links = a.open_html_and_parse()
st.write(T_headlines_and_links[0][0])'''
'''a = DailyMailPipeline(urls=daily_mail_urls)
#a.get_topic_page_response()
DM_headlines_and_links = a.open_html_and_parse()
st.write(DM_headlines_and_links[1][1])'''

'''
a = GuardianPipeline('trans')
#a.get_topic_page_response()
G_headlines_and_links = a.get_headline_and_links()

b = IndependentPipeline('ya')
I_headlines_and_links = b.get_headline_and_links()


def list_of_headlines():
    DM_headlines = DM_headlines_and_links[0]
    G_headlines = G_headlines_and_links[0]
    I_headlines = I_headlines_and_links[0]
    return DM_headlines, G_headlines, I_headlines 



def links():
    DM_links = DM_headlines_and_links[1]
    G_links = G_headlines_and_links[1]
    I_links = I_headlines_and_links[1]
    return DM_links, G_links, I_links

def sort_links(links):
    for index, value in enumerate(links):
        links[index] = f"<a  href='{links[index]}'>View Article</a>"
    return(links)

DM_links = DM_headlines_and_links[1]
G_links = G_headlines_and_links[1]
I_links = I_headlines_and_links[1]
DM_links = sort_links(DM_links)
G_links = sort_links(G_links)
I_links = sort_links(I_links)

select = st.select_slider(label='timeline', options =('Left', 'Center', 'Right'), value = 'Center', label_visibility='collapsed')

if select == 'Center':
    data = {'Source':'https://tonyrobertson.mycouncillor.org.uk/files/2016/03/The-Independent-Logo.gif', 'Headline': I_headlines_and_links[0], 'Link': I_links}
if select == 'Left':
    data = {'Source':'https://upload.wikimedia.org/wikipedia/commons/thumb/7/75/The_Guardian_2018.svg/2560px-The_Guardian_2018.svg.png','Headline': G_headlines_and_links[0], 'Links': G_links }
if select == 'Right':
    data = {'Source':'https://image.pngaaa.com/480/3881480-middle.png', 'Headline':DM_headlines_and_links[0], 'Link': DM_links }

df = (pd.DataFrame(data))
hide_table_row_index = """
            <style>

            thead tr th:first-child {display:none}
            tbody th {display:none}
            
            </style>
            """


st.markdown("<h1 style='text-align: center;color: black;'>Trans Issues</h1>", unsafe_allow_html=True)

st.write('')


with st.expander('**Principles** ', expanded=True):
    columns = st.columns(3)
    columns[0].write('Left')
    st.write('')


with st.expander('**Headlines**', expanded=True):
    st.write('')

        # Inject CSS with Markdown
    st.markdown(hide_table_row_index, unsafe_allow_html=True)

    df_html = table_with_images(df=df, url_columns=('Source',))
    st.markdown(df_html, unsafe_allow_html=True)

    # only grab articles from guardian

with st.expander('**Videos**', expanded=True):
    cols = st.columns(2)
    cols[0].video('https://www.youtube.com/watch?v=TBJGgCHgf5w')

    cols[1].video('https://www.youtube.com/watch?v=TBJGgCHgf5w') '''