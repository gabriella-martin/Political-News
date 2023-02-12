import requests
from bs4 import BeautifulSoup

import streamlit as st
from streamlit_extras.image_in_tables import table_with_images

import pandas as pd

daily_mail_topics = ['black-lives-matter', 'brexit', 'climate_change_global_warming', 'nhs', 'transgender-issues', 'uk-economy']  

class DailyMailPipeline:

    def __init__(self, topic):
        self.topic = topic
        self.recent_ten_headlines = []
        self.recent_ten_links = []
    def get_topic_page_response(self):

        url = f'https://www.dailymail.co.uk/home/search.html?topic=Transgender+Issues'
        r = requests.get(url)
        with open('DM-{self.topic}', 'wb') as f:
            f.write(r.content)
    
    def open_html_and_parse(self):
        with open('DM-{self.topic}', 'rb') as f:
            soup = BeautifulSoup(f.read(), 'html.parser')
        
        return soup
    
    def get_headline_and_link(self):
        soup = self.open_html_and_parse()
        topic_articles = soup.find_all("div", class_="sch-result news cleared")
        num = 0
        for i in topic_articles:
            if num < 11:
                link = i.a['href']
                link = 'https://www.dailymail.co.uk' + link
                headline = i.div.h3.text
                self.recent_ten_headlines.append(headline)
                self.recent_ten_links.append(link)
                num +=1
        return self.recent_ten_headlines, self.recent_ten_links


a = DailyMailPipeline('trans')
#a.get_topic_page_response()
DM_headlines_and_links = a.get_headline_and_link()

class GuardianPipeline:
    def __init__(self, topic):
        self.topic = topic
        self.recent_ten_headlines = []
        self.recent_ten_links = []

    def get_topic_page_response(self):

        url = f'https://www.theguardian.com/society/transgender'
        r = requests.get(url)
        with open(f'DM-{self.topic}', 'wb') as f:
            f.write(r.content)
    
    def open_html_and_parse(self):
        with open('DM-trans', 'rb') as f:
            soup = BeautifulSoup(f.read(), 'html.parser')
        
        return soup

    def get_headline_and_links(self):

        soup = self.open_html_and_parse()
        topic_articles = soup.find_all("li", class_="fc-slice__item l-row__item l-row__item--span-1 u-faux-block-link")
        num = 0
        for i in topic_articles:
            link = i.a['href']
            headline = i.div.span.text
            self.recent_ten_headlines.append(headline)
            self.recent_ten_links.append(link)
            num += 1
        if num <10:
            topic_articles = soup.find_all('li', class_ = 'fc-slice__item l-list__item l-row__item l-row__item--span-1 u-faux-block-link' )
            for i in topic_articles:
                if num <10:
                    link = i.a['href']
                    headline = i.div.span.text
                    self.recent_ten_headlines.append(headline)
                    self.recent_ten_links.append(link)
                    num += 1
                else:
                    break
        return self.recent_ten_headlines, self.recent_ten_links

a = GuardianPipeline('trans')
#a.get_topic_page_response()
G_headlines_and_links = a.get_headline_and_links()

select = st.select_slider(label='timeline', options =('Left', 'Center', 'Right'), value = 'Center', label_visibility='collapsed')

DM_links = DM_headlines_and_links[1]
G_links = G_headlines_and_links[1]

def sort_links(links):
    for index, value in enumerate(links):
        links[index] = f"<a  href='{links[index]}'>View article</a>"
    return(links)


DM_links = sort_links(DM_links)
G_links = sort_links(G_links)

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

# Inject CSS with Markdown
st.markdown(hide_table_row_index, unsafe_allow_html=True)

df_html = table_with_images(df=df, url_columns=('Source',))
st.markdown(df_html, unsafe_allow_html=True)

# only grab articles from guardian