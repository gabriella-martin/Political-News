import requests
from bs4 import BeautifulSoup

import streamlit as st


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
                headline = i.div.h3.text
                self.recent_ten_headlines.append(headline)
                self.recent_ten_links.append(link)
                num +=1
        return self.recent_ten_headlines, self.recent_ten_links


a = DailyMailPipeline('trans')
#a.get_topic_page_response()
headlines_and_links = a.get_headline_and_link()




for i in headlines_and_links[0]:
    st.write(i)



class 