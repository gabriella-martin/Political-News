import pickle
import requests
from bs4 import BeautifulSoup

# RIGHT WING PIPELINE

the_times_urls = ["https://www.thetimes.co.uk/search?filter=all&q=transgender&source=search-page", 'https://www.thetimes.co.uk/search?source=search-page&q=immigration', 'https://www.thetimes.co.uk/search?source=search-page&q=racism', 'https://www.thetimes.co.uk/search?source=search-page&q=brexit' ]
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
                        headline = (i.span.text)[1:-1]
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
                topic_articles = soup.find_all('div', class_ ='sc-lg3v5c-0 hJgjOp sc-lg3v5c-2 jJLexE hero-article article-default')
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


if __name__ == '__main__':

    rw1 = TheTimesPipeline(urls=the_times_urls) 
    rw1.get_topic_page_response()
    rw1_head_links = rw1.open_html_and_parse()

    rw2 = TelegraphPipeline(urls=telegraph_urls)
    rw2.get_topic_page_response()
    rw2_head_links = rw2.open_html_and_parse()

    lw1 = GuardianPipeline(urls=guardian_urls)
    lw1.get_topic_page_response()
    lw1_head_links = lw1.open_html_and_parse()

    lw2 = IndependentPipeline(urls=independent_urls)
    lw2.get_topic_page_response()
    lw2_head_links = lw2.open_html_and_parse()


    n = INewsPipeline(urls=i_news_links)
    n.get_topic_page_response()
    n_head_links = n.open_html_and_parse()


headlines = [rw1_head_links[0], rw2_head_links[0], lw1_head_links[0], lw2_head_links[0], n_head_links[0]] 
links_before_formatted = [rw1_head_links[1], rw2_head_links[1], lw1_head_links[1], lw2_head_links[1], n_head_links[1]]

def sort_links(links_before_formatted):
    list_of_links = []
    for link in links_before_formatted:
        for topic in link:
            for index, value in enumerate(topic):
                topic[index] = f"<a  href='{topic[index]}'>View Article</a>"
        list_of_links.append(links_before_formatted)
    return(list_of_links)


links = sort_links(links_before_formatted)

with open('data/links', 'wb') as l:
        pickle.dump(links, l)

with open('data/headlines', 'wb') as h:
        pickle.dump(headlines, h)
